import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { Slot } from "radix-ui"
import { Loader2 } from "lucide-react"
import { cn } from "@/lib/utils"

const primary =
  "bg-brand text-fg-on-brand hover:shadow-button-hover active:shadow-none " +
  "motion-safe:hover:scale-[1.03] motion-safe:active:scale-[0.98] " +
  // Reduced motion: no scale, colour steps instead (brand 600 hover, 700 pressed).
  "motion-reduce:hover:bg-brand-600 motion-reduce:active:bg-brand-700"

const buttonVariants = cva(
  "inline-flex shrink-0 items-center justify-center gap-2 rounded-full font-sans font-medium whitespace-nowrap select-none " +
    "transition-[transform,background-color,box-shadow,color,border-color] duration-200 ease-standard " +
    "focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus-ring " +
    "disabled:pointer-events-none disabled:opacity-40 aria-disabled:pointer-events-none aria-disabled:opacity-40 " +
    "aria-invalid:outline-2 aria-invalid:outline-error " +
    "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
  {
    variants: {
      variant: {
        primary,
        /** shadcn compatibility alias of `primary`. */
        default: primary,
        secondary:
          "border border-line-strong bg-transparent text-fg-heading hover:border-fg-muted hover:bg-surface-hover active:bg-surface-raised",
        ghost: "bg-transparent text-fg-body hover:bg-surface-hover hover:text-fg-heading active:bg-surface-raised",
        destructive: "border border-error/55 bg-error/10 text-fg-error hover:bg-error/14 active:bg-error/18",
        link: "h-auto rounded-xs px-0 text-fg-brand underline-offset-4 hover:underline active:opacity-80",
      },
      size: {
        sm: "h-9 px-4 text-sm",
        default: "h-11 px-6 text-[15px]",
        lg: "h-13 px-8 text-base",
        icon: "size-11",
        "icon-sm": "size-9",
      },
    },
    compoundVariants: [{ variant: "link", className: "h-auto px-0" }],
    defaultVariants: { variant: "primary", size: "default" },
  }
)

type ButtonProps = React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
    /** Shows a spinner, sets aria-busy and blocks interaction. */
    loading?: boolean
  }

function Button({ className, variant, size, asChild = false, loading = false, disabled, children, ...props }: ButtonProps) {
  const Comp = asChild ? Slot.Root : "button"
  return (
    <Comp
      data-slot="button"
      data-variant={variant ?? "primary"}
      data-size={size ?? "default"}
      aria-busy={loading || undefined}
      disabled={asChild ? undefined : disabled || loading}
      aria-disabled={asChild && (disabled || loading) ? true : undefined}
      className={cn(buttonVariants({ variant, size }), className)}
      {...props}
    >
      {loading && !asChild ? (
        <>
          <Loader2 aria-hidden className="motion-safe:animate-spin" />
          {children}
        </>
      ) : (
        children
      )}
    </Comp>
  )
}

export { Button, buttonVariants }
export type { ButtonProps }
