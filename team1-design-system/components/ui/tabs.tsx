"use client"

import * as React from "react"
import { Tabs as TabsPrimitive } from "radix-ui"
import { cn } from "@/lib/utils"

function Tabs({ className, ...props }: React.ComponentProps<typeof TabsPrimitive.Root>) {
  return <TabsPrimitive.Root data-slot="tabs" className={cn("flex min-w-0 max-w-full flex-col gap-4", className)} {...props} />
}

function TabsList({ className, ...props }: React.ComponentProps<typeof TabsPrimitive.List>) {
  return (
    <TabsPrimitive.List
      data-slot="tabs-list"
      className={cn("inline-flex w-fit max-w-full items-center gap-1 overflow-x-auto rounded-full border border-line bg-surface p-1 [scrollbar-width:none]", className)}
      {...props}
    />
  )
}

function TabsTrigger({ className, ...props }: React.ComponentProps<typeof TabsPrimitive.Trigger>) {
  return (
    <TabsPrimitive.Trigger
      data-slot="tabs-trigger"
      className={cn(
        "inline-flex h-9 items-center justify-center gap-1.5 rounded-full px-4 text-sm font-medium whitespace-nowrap text-fg-muted transition-colors duration-150",
        "hover:text-fg-heading focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus-ring",
        "data-[state=active]:bg-surface-hover data-[state=active]:text-fg-heading disabled:pointer-events-none disabled:opacity-40",
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        className
      )}
      {...props}
    />
  )
}

function TabsContent({ className, ...props }: React.ComponentProps<typeof TabsPrimitive.Content>) {
  return (
    <TabsPrimitive.Content
      data-slot="tabs-content"
      className={cn("rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus-ring", className)}
      {...props}
    />
  )
}

export { Tabs, TabsList, TabsTrigger, TabsContent }
