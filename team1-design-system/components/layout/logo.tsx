import * as React from "react"
import { cn } from "@/lib/utils"

type LogoProps = {
  /** Authentic Team1_MAIN_WHITE.svg (red symbol + white wordmark) for dark backgrounds. */
  onDarkSrc: string
  /** Authentic Team1_BLACK_MAIN.svg (red symbol + black wordmark) for light backgrounds. */
  onLightSrc: string
  href?: string
  className?: string
  /** Optional product/chapter label shown beside (never inside) the logo. */
  label?: string
}

/** Swaps the two authentic logo files by theme. Never recolour, redraw or apply effects to the mark. */
function Logo({ onDarkSrc, onLightSrc, href = "/", className, label }: LogoProps) {
  return (
    <a
      href={href}
      className={cn("inline-flex items-center gap-3 rounded-xs focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-focus-ring", className)}
    >
      <img src={onDarkSrc} alt="Team1" width={96} height={27} className="h-6 w-auto theme-light:hidden" />
      <img src={onLightSrc} alt="Team1" width={96} height={27} className="hidden h-6 w-auto theme-light:block" />
      {label ? (
        <span className="border-l border-line-strong pl-3 text-sm font-normal text-fg-muted">{label}</span>
      ) : null}
    </a>
  )
}

export { Logo }
export type { LogoProps }
