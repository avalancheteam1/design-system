export type Team1Theme = "dark" | "light"
const STORAGE_KEY = "team1-theme"

/** Explicit user choice, if any. Without one, CSS follows prefers-color-scheme and defaults to dark. */
export function getStoredTheme(): Team1Theme | null {
  try {
    const value = localStorage.getItem(STORAGE_KEY)
    return value === "dark" || value === "light" ? value : null
  } catch {
    return null
  }
}

export function resolvedTheme(): Team1Theme {
  const explicit = document.documentElement.getAttribute("data-theme")
  if (explicit === "dark" || explicit === "light") return explicit
  return window.matchMedia?.("(prefers-color-scheme: light)").matches ? "light" : "dark"
}

export function setTheme(theme: Team1Theme | null) {
  const root = document.documentElement
  if (theme) root.setAttribute("data-theme", theme)
  else root.removeAttribute("data-theme")
  try {
    if (theme) localStorage.setItem(STORAGE_KEY, theme)
    else localStorage.removeItem(STORAGE_KEY)
  } catch {
    /* storage unavailable: the choice lasts for this page view */
  }
}

/** Inline this in <head> before first paint to avoid a theme flash. */
export const themeBootScript = `(function(){try{var t=localStorage.getItem("${STORAGE_KEY}");if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t)}catch(e){}})()`
