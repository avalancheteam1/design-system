import * as React from "react"
import { cn } from "@/lib/utils"

/** Field family (Input, Textarea, Select) shares radius-sm (12px), the >=3:1 input border and the 2px focus ring. */
const fieldClass =
  "w-full min-w-0 rounded-sm border border-input-border bg-surface text-base font-normal text-fg-heading md:text-sm " +
  "placeholder:text-fg-muted transition-[border-color,background-color] duration-150 " +
  "hover:border-fg-muted focus-visible:border-fg-heading focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus-ring " +
  "disabled:cursor-not-allowed disabled:opacity-40 " +
  "aria-invalid:border-error aria-invalid:outline-error"

function Input({ className, type, ...props }: React.ComponentProps<"input">) {
  return <input type={type} data-slot="input" className={cn(fieldClass, "h-11 px-3.5", className)} {...props} />
}

export { Input, fieldClass }
