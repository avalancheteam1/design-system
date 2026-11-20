import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { Slot } from "radix-ui"
import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex w-fit shrink-0 items-center justify-center gap-1 rounded-full border px-2.5 py-0.5 text-xs leading-5 font-medium whitespace-nowrap [&>svg]:pointer-events-none [&>svg]:size-3 " +
    "focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus-ring",
  {
    variants: {
      variant: {
        brand: "border-brand/35 bg-brand/10 text-fg-brand theme-light:text-brand-700",
        solid: "border-transparent bg-brand text-white",
        neutral: "border-line-strong bg-surface-raised text-fg-body",
        outline: "border-line-strong bg-transparent text-fg-body",
        success: "border-success/40 bg-success/10 text-fg-success",
        warning: "border-warning/45 bg-warning/10 text-fg-warning",
        error: "border-error/45 bg-error/10 text-fg-error",
      },
    },
    defaultVariants: { variant: "neutral" },
  }
)

function Badge({ className, variant, asChild = false, ...props }: React.ComponentProps<"span"> & VariantProps<typeof badgeVariants> & { asChild?: boolean }) {
  const Comp = asChild ? Slot.Root : "span"
  return <Comp data-slot="badge" data-variant={variant ?? "neutral"} className={cn(badgeVariants({ variant }), className)} {...props} />
}

export { Badge, badgeVariants }
