"use client"

import * as React from "react"
import { MoonIcon, SunIcon } from "lucide-react"
import { Button } from "@/components/ui/button"
import { resolvedTheme, setTheme, type Team1Theme } from "@/lib/theme"

function ThemeToggle() {
  const [theme, setLocal] = React.useState<Team1Theme>("dark")
  React.useEffect(() => setLocal(resolvedTheme()), [])
  const next: Team1Theme = theme === "dark" ? "light" : "dark"
  return (
    <Button
      variant="ghost"
      size="icon-sm"
      aria-label={`Switch to ${next} theme`}
      onClick={() => {
        setTheme(next)
        setLocal(next)
      }}
    >
      {theme === "dark" ? <SunIcon aria-hidden /> : <MoonIcon aria-hidden />}
    </Button>
  )
}

export { ThemeToggle }
