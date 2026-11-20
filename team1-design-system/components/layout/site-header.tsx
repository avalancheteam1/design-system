"use client"

import * as React from "react"
import { MenuIcon, XIcon } from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import { Logo, type LogoProps } from "./logo"

type NavLink = { label: string; href: string; active?: boolean }

type SiteHeaderProps = {
  logo: LogoProps
  links: NavLink[]
  /** Right-hand actions, e.g. ThemeToggle + Sign in + primary Join button. */
  actions?: React.ReactNode
  className?: string
}

function SiteHeader({ logo, links, actions, className }: SiteHeaderProps) {
  const [open, setOpen] = React.useState(false)
  const linkClass = (active?: boolean) =>
    cn(
      "rounded-full px-3 py-2 text-sm font-normal transition-colors duration-150 hover:text-fg-heading focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus-ring",
      active ? "text-fg-heading" : "text-fg-muted"
    )
  return (
    <header
      data-slot="site-header"
      className={cn("sticky top-0 z-[var(--team1-z-navbar)] border-b border-line bg-background/80 backdrop-blur-md", className)}
    >
      <div className="container-page flex h-16 items-center justify-between gap-4">
        <Logo {...logo} />
        <nav aria-label="Main" className="hidden items-center gap-1 md:flex">
          {links.map((l) => (
            <a key={l.href} href={l.href} aria-current={l.active ? "page" : undefined} className={linkClass(l.active)}>
              {l.label}
            </a>
          ))}
        </nav>
        <div className="flex items-center gap-2">
          {actions}
          <Button
            variant="ghost"
            size="icon-sm"
            className="md:hidden"
            aria-expanded={open}
            aria-controls="team1-mobile-nav"
            aria-label={open ? "Close menu" : "Open menu"}
            onClick={() => setOpen((v) => !v)}
          >
            {open ? <XIcon aria-hidden /> : <MenuIcon aria-hidden />}
          </Button>
        </div>
      </div>
      {open ? (
        <nav id="team1-mobile-nav" aria-label="Main" className="container-page flex flex-col gap-1 border-t border-line py-3 md:hidden">
          {links.map((l) => (
            <a key={l.href} href={l.href} aria-current={l.active ? "page" : undefined} className={cn(linkClass(l.active), "py-3")}>
              {l.label}
            </a>
          ))}
        </nav>
      ) : null}
    </header>
  )
}

export { SiteHeader }
export type { NavLink, SiteHeaderProps }
