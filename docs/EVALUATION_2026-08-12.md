# Team1 design-system v2 clean-room evaluation

## Method

Three independent agent trials used the exact prompts and 10-criterion rubrics below. Each trial ran without access to its rubric, prior answer, or score report: the agent read the live packaged skill and applicable modules, then produced only the requested handoff. A separate strict scorer reviewed the frozen response. Each criterion scores 0–2; an evaluation passes at 18/20 with no hard fail.

The baseline conditions were preserved before v2 implementation. The final-response hashes below bind this report to the evaluated outputs without publishing private Drive identifiers or member information.

## Scenarios

| Scenario | Required behaviors |
|---|---|
| Public chapter web launch | Reject stale red/type/logo shortcuts; apply current identity, complete tokens/assets, accessible interaction and motion, responsive/real-device QA, and go-live governance |
| Current presentation master | Reject the old overview; use the packaged 40-exemplar, 20-layout-part, one-master source; preserve inherited construction; enforce rights/QR/editability/export QA |
| Regional event kit | Reject stale chapter/QR/media; apply current identity plus presentation exception, format-specific layouts, localization, rights, co-branding, print proofing, and final ledgers |

## Baselines

| Condition | Web | Presentation | Regional event | Combined | Passed | Hard fails |
|---|---:|---:|---:|---:|---:|---:|
| No skill | 6/20 | 9/20 | 12/20 | 27/60 | 0/3 | 1 |
| v1.0.0 | 9/20 | 11/20 | 13/20 | 33/60 | 0/3 | 3 |

## Final v2 rerun

Final values are inserted only after all three clean-room responses have been frozen and independently rescored.

| Scenario | Score | Result | Hard fail | Response SHA-256 |
|---|---:|---|---|---|
| Public chapter web launch | 19/20 | PASS | none | `fe232b9484cc9c27115ed0671c6614c1daa2cda3b069192e4f35eb0ae3f747ff` |
| Current presentation master | 20/20 | PASS | none | `b3a76ce01c5752bf81b02fd994dfab0dae2edc157a4c56e38400c0dc1152c821` |
| Regional event kit | 20/20 | PASS | none | `9ab72aed9949895615600d224508506fc17eee000a69efa92e780ad6ce03b5fe` |
| **Combined** | **59/60 (98.33%)** | **3/3 PASS** | **none** | — |

The presentation source count is physical package evidence: 40 slide parts, 20 slide-layout parts, and one slide-master part in the released font-clean PPTX. The web response earned full credit on 9/10 criteria; the strict scorer awarded 1/2 on naming because it stated the title/proper-name and flowing-copy boundary but did not explicitly repeat the sentence-start boundary. It still passed with no hard fail.

V2 improved the combined result by 32 points over no skill and 26 points over v1, moved all three scenarios above the pass threshold, and eliminated all hard fails.

## Reproduction and acceptance

The prompts, rubrics, responses, and detailed criterion rationales remain in the private release audit workspace. To reproduce, freeze the package commit, give a clean agent only `SKILL.md`, its routed modules, and one prompt, hash the response, then score it independently against the corresponding rubric.

This evaluation measures whether the package reliably elicits the required production contract. It does not replace brand-owner, rights, privacy, partner, destination, or publication approval for a real artifact.
