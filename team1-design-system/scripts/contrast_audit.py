#!/usr/bin/env python3
"""WCAG 2.2 contrast audit for the Team1 web theme tokens (design system 3.0.0).

Reads tokens/design-tokens.json and writes tokens/CONTRAST.md. Translucent values are
alpha-blended over the surface they sit on, exactly as the components use them.

  python3 scripts/contrast_audit.py          # write tokens/CONTRAST.md
  python3 scripts/contrast_audit.py --check  # exit 1 if a required pair fails or the file is stale
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
TOKENS = PKG / "tokens" / "design-tokens.json"
OUT = PKG / "tokens" / "CONTRAST.md"


def parse(value: str) -> tuple[float, float, float, float]:
    value = value.strip()
    if value.startswith("#"):
        h = value[1:]
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0
    m = re.match(r"rgba?\(([^)]+)\)", value)
    if not m:
        raise ValueError(value)
    parts = [p.strip() for p in m.group(1).replace("/", ",").split(",") if p.strip()]
    r, g, b = (float(p) for p in parts[:3])
    a = float(parts[3]) if len(parts) > 3 else 1.0
    return r, g, b, a


def blend(fg: str | tuple, bg: str | tuple, alpha: float | None = None) -> tuple[float, float, float]:
    f = parse(fg) if isinstance(fg, str) else fg
    b = parse(bg) if isinstance(bg, str) else bg
    a = f[3] if alpha is None else alpha
    return tuple(f[i] * a + b[i] * (1 - a) for i in range(3))  # type: ignore[return-value]


def lum(rgb) -> float:
    def ch(c: float) -> float:
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb[:3]
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ratio(a, b) -> float:
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hexof(rgb) -> str:
    return "#" + "".join(f"{round(c):02x}" for c in rgb[:3])


def v(node) -> str:
    return node["$value"] if isinstance(node, dict) else node


def audit() -> tuple[list[dict], list[dict]]:
    data = json.loads(TOKENS.read_text())
    web = data["web"]["theme"]
    status = {k: v(x) for k, x in data["global"]["color"]["status"].items() if not k.startswith("$")}
    scale = {k: v(x) for k, x in data["global"]["color"]["brand"]["scale"].items() if not k.startswith("$")}
    rows: list[dict] = []
    nontext: list[dict] = []

    for theme in ("dark", "light"):
        t = {k: v(x) for k, x in web[theme].items() if not k.startswith("$")}
        bg = parse(t["background"])
        grounds = {
            "background": bg,
            "surface": parse(t["surface"]),
            "surfaceRaised": parse(t["surfaceRaised"]),
            "surfaceHover": parse(t["surfaceHover"]),
        }

        def add(fg_name, fg_rgb, bg_name, bg_rgb, use, need=4.5, required=True):
            r = ratio(fg_rgb, bg_rgb)
            rows.append({"theme": theme, "fg": fg_name, "fgv": hexof(fg_rgb), "bg": bg_name, "bgv": hexof(bg_rgb),
                         "ratio": r, "need": need, "pass": r >= need, "required": required, "use": use})

        body_roles = {"textHeading": "headings, titles", "textBody": "body copy", "textMuted": "secondary text, captions, placeholders"}
        for role, use in body_roles.items():
            for gname, g in grounds.items():
                add(role, parse(t[role]), gname, g, use)
        for role, use in {"textBrand": "red text: links, kickers, inline emphasis", "textError": "error messages",
                          "textSuccess": "success text", "textWarning": "warning text"}.items():
            for gname in ("background", "surface", "surfaceRaised"):
                add(role, parse(t[role]), gname, grounds[gname], use)
            # hover surface: allowed only where the pair passes; flag otherwise
            add(role, parse(t[role]), "surfaceHover", grounds["surfaceHover"], use + " (on hover surface)",
                required=role != "textBrand")

        white = parse(t["textOnBrand"])
        for step, label in (("500", "primary button / solid badge rest"), ("600", "primary hover, reduced motion"),
                            ("700", "primary pressed, reduced motion")):
            add("textOnBrand", white, f"red {step}", parse(scale[step]), label)
        # tinted components: tint alpha blended over the page background
        tints = [
            ("textBrand" if theme == "dark" else "red 700", "brand", scale["500"], 0.10, "brand badge (light theme uses red 700 text)"),
            ("textError", "error", status["error"], 0.10, "error badge, destructive button rest"),
            ("textError", "error", status["error"], 0.14, "destructive button hover"),
            ("textError", "error", status["error"], 0.18, "destructive button pressed"),
            ("textSuccess", "success", status["success"], 0.10, "success badge"),
            ("textWarning", "warning", status["warning"], 0.10, "warning badge"),
            ("textBody", "success", status["success"], 0.08, "success alert body"),
            ("textBody", "warning", status["warning"], 0.08, "warning alert body"),
            ("textBody", "error", status["error"], 0.08, "error alert body"),
        ]
        for role, tname, tint, a, use in tints:
            for gname in ("background", "surface", "surfaceRaised"):
                g = blend(tint, grounds[gname], a)
                fg = parse(scale["700"]) if role == "red 700" else parse(t[role])
                add(role, fg, f"{tname} {int(a*100)}% over {gname}", g, use)

        # Non-text (WCAG 1.4.11, 3:1): field borders, focus ring, control boundaries
        def nt(name, fg_rgb, bg_name, bg_rgb, use, need=3.0, required=True):
            r = ratio(fg_rgb, bg_rgb)
            nontext.append({"theme": theme, "fg": name, "fgv": hexof(fg_rgb), "bg": bg_name, "bgv": hexof(bg_rgb),
                            "ratio": r, "need": need, "pass": r >= need, "required": required, "use": use})

        for gname in ("background", "surface"):
            nt("inputBorder", blend(t["inputBorder"], grounds[gname]), gname, grounds[gname], "input, select, checkbox, switch-off boundary")
            nt("focusRing", parse(t["focusRing"]), gname, grounds[gname], "2px focus outline")
        nt("red 500", parse(scale["500"]), "background", bg, "checked checkbox / switch-on, primary button shape")
        nt("borderStrong", blend(t["borderStrong"], bg), "background", bg, "secondary button outline (label carries meaning)", required=False)
        nt("border", blend(t["border"], bg), "background", bg, "decorative card / divider line", required=False)
    return rows, nontext


def render(rows, nontext) -> str:
    def table(items):
        out = ["| Theme | Foreground | Background | Ratio | Needs | Result | Used for |", "|---|---|---|---:|---:|---|---|"]
        for r in items:
            res = "pass" if r["pass"] else ("FAIL" if r["required"] else "below (not allowed)" if r["need"] >= 4.5 else "below (decorative)")
            out.append(f"| {r['theme']} | `{r['fg']}` {r['fgv']} | `{r['bg']}` {r['bgv']} | {r['ratio']:.2f} | {r['need']:g} | {res} | {r['use']} |")
        return "\n".join(out)

    req = [r for r in rows + nontext if r["required"]]
    failed = [r for r in req if not r["pass"]]
    body = [r for r in rows if r["fg"] in ("textHeading", "textBody", "textMuted")]
    lines = [
        "# Web contrast audit — Team1 Design System 3.0.0",
        "",
        "Generated by `scripts/contrast_audit.py` from `tokens/design-tokens.json` (`web.theme.*`). Do not edit by hand.",
        "Translucent tints and borders are alpha-blended over the ground they sit on. Text needs 4.5:1 (WCAG 2.2 AA 1.4.3, normal size);",
        "UI component boundaries and focus indicators need 3:1 (1.4.11).",
        "",
        f"**Summary:** {len(req) - len(failed)} of {len(req)} required pairs pass. "
        f"Body-text pairs (heading/body/muted on every ground): {sum(r['pass'] for r in body)} of {len(body)} pass. "
        f"{'No required pair fails.' if not failed else 'FAILING: ' + ', '.join(r['fg'] + ' on ' + r['bg'] for r in failed)}",
        "",
        "Rows marked *below (not allowed)* are pairs the system forbids rather than fixes: red text (`textBrand`) must not sit on the",
        "hover surface; use `textHeading` there. Rows marked *below (decorative)* are hairlines that never carry meaning on their own.",
        "",
        "## Text",
        "",
        table(rows),
        "",
        "## Non-text (1.4.11)",
        "",
        table(nontext),
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    rows, nontext = audit()
    text = render(rows, nontext)
    failed = [r for r in rows + nontext if r["required"] and not r["pass"]]
    if "--check" in sys.argv:
        stale = not OUT.exists() or OUT.read_text() != text
        if stale:
            print("tokens/CONTRAST.md is stale: run scripts/contrast_audit.py")
        for r in failed:
            print(f"FAIL {r['theme']} {r['fg']} on {r['bg']}: {r['ratio']:.2f} < {r['need']}")
        return 1 if (stale or failed) else 0
    OUT.write_text(text)
    print(f"wrote {OUT.relative_to(PKG)}; {len(failed)} required failures")
    for r in failed:
        print(f"FAIL {r['theme']} {r['fg']} on {r['bg']}: {r['ratio']:.2f} < {r['need']}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
