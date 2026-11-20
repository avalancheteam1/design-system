"use client"

import * as React from "react"
import { Checkbox as CheckboxPrimitive } from "radix-ui"
import { CheckIcon } from "lucide-react"
import { cn } from "@/lib/utils"

function Checkbox({ className, ...props }: React.ComponentProps<typeof CheckboxPrimitive.Root>) {
  return (
    <CheckboxPrimitive.Root
      data-slot="checkbox"
      className={cn(
        // radius-xs (6px): a 12px corner on an 18px box would read as a radio button.
        "peer size-[18px] shrink-0 rounded-xs border border-input-border bg-surface transition-colors duration-150",
        "hover:border-fg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus-ring",
        "data-[state=checked]:border-brand data-[state=checked]:bg-brand data-[state=checked]:text-white",
        "disabled:cursor-not-allowed disabled:opacity-40 aria-invalid:border-error",
        className
      )}
      {...props}
    >
      <CheckboxPrimitive.Indicator data-slot="checkbox-indicator" className="flex items-center justify-center text-current">
        <CheckIcon aria-hidden className="size-3.5" strokeWidth={3} />
      </CheckboxPrimitive.Indicator>
    </CheckboxPrimitive.Root>
  )
}

export { Checkbox }
