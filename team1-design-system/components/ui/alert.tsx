import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

// Info is neutral by design (red is the only UI accent). Status is never colour-only: always pair with an icon and a title.
const alertVariants = cva(
  "relative grid w-full grid-cols-[0_1fr] items-start gap-y-1 rounded-sm border px-4 py-3.5 text-sm font-normal has-[>svg]:grid-cols-[1.25rem_1fr] has-[>svg]:gap-x-3 [&>svg]:size-5 [&>svg]:translate-y-px",
  {
    variants: {
      variant: {
        info: "border-line-strong bg-surface text-fg-body [&>svg]:text-fg-heading",
        success: "border-success/40 bg-success/8 text-fg-body [&>svg]:text-fg-success",
        warning: "border-warning/45 bg-warning/8 text-fg-body [&>svg]:text-fg-warning",
        error: "border-error/45 bg-error/8 text-fg-body [&>svg]:text-fg-error",
      },
    },
    defaultVariants: { variant: "info" },
  }
)

function Alert({ className, variant, ...props }: React.ComponentProps<"div"> & VariantProps<typeof alertVariants>) {
  const role = variant === "error" || variant === "warning" ? "alert" : "status"
  return <div data-slot="alert" data-variant={variant ?? "info"} role={role} className={cn(alertVariants({ variant }), className)} {...props} />
}

function AlertTitle({ className, ...props }: React.ComponentProps<"div">) {
  return <div data-slot="alert-title" className={cn("col-start-2 font-medium text-fg-heading", className)} {...props} />
}

function AlertDescription({ className, ...props }: React.ComponentProps<"div">) {
  return <div data-slot="alert-description" className={cn("col-start-2 text-fg-muted [&_p]:leading-relaxed", className)} {...props} />
}

export { Alert, AlertTitle, AlertDescription, alertVariants }
