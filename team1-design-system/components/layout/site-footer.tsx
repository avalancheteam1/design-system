import * as React from "react"
import { ArrowUpRight } from "lucide-react"
import { cn } from "@/lib/utils"
import { Logo, type LogoProps } from "./logo"

type FooterColumn = { title: string; links: { label: string; href: string; external?: boolean }[] }

type SiteFooterProps = {
  logo: LogoProps
  columns: FooterColumn[]
  /** Big closing line. Defaults to the hub's "Keep building." */
  tagline?: React.ReactNode
  legal?: React.ReactNode
  className?: string
}

function SiteFooter({ logo, columns, tagline, legal, className }: SiteFooterProps) {
  return (
    <footer data-slot="site-footer" className={cn("border-t border-line bg-surface", className)}>
      <div className="container-page grid gap-12 py-14 lg:grid-cols-[1fr_1.2fr] lg:py-20">
        <div className="flex flex-col gap-8">
          <Logo {...logo} />
          <p className="font-heading text-[clamp(2.75rem,6vw,5.5rem)] leading-[0.9] font-medium tracking-[-0.04em] text-fg-heading">
            {tagline ?? (
              <>
                Keep
                <br />
                <span className="text-brand">building.</span>
              </>
            )}
          </p>
        </div>
        <nav aria-label="Footer" className="grid grid-cols-2 gap-8 self-end sm:grid-cols-3">
          {columns.map((c) => (
            <div key={c.title}>
              <p className="meta mb-4">{c.title}</p>
              <ul className="space-y-2">
                {c.links.map((l) => (
                  <li key={l.href}>
                    <a
                      href={l.href}
                      {...(l.external ? { target: "_blank", rel: "noopener noreferrer" } : {})}
                      className="group inline-flex items-center gap-1 rounded-xs text-sm font-normal text-fg-body transition-colors hover:text-fg-heading focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus-ring"
                    >
                      {l.label}
                      {l.external ? <ArrowUpRight aria-hidden className="size-3.5 text-fg-muted group-hover:text-fg-brand" /> : null}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </nav>
      </div>
      <div className="border-t border-line">
        <div className="container-page flex flex-col gap-2 py-5 sm:flex-row sm:items-center sm:justify-between">
          <p className="meta">{legal ?? `© ${new Date().getFullYear()} Team1`}</p>
        </div>
      </div>
    </footer>
  )
}

export { SiteFooter }
export type { FooterColumn, SiteFooterProps }
