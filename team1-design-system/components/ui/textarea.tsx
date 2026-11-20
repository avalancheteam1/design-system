import * as React from "react"
import { cn } from "@/lib/utils"
import { fieldClass } from "./input"

function Textarea({ className, ...props }: React.ComponentProps<"textarea">) {
  return (
    <textarea
      data-slot="textarea"
      className={cn(fieldClass, "field-sizing-content min-h-24 px-3.5 py-3 leading-[1.45]", className)}
      {...props}
    />
  )
}

export { Textarea }
