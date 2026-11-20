import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const cardVariants = cva("flex flex-col gap-5 rounded-lg border bg-surface py-6 text-fg-body", {
  variants: {
    variant: {
      /** Default Team1 card: soft red glow (www style). */
      glow: "border-line shadow-card",
      /** Dense lists, dashboards, nested content: border only, no glow. */
      quiet: "border-line shadow-none",
    },
    interactive: { true: "transition-[box-shadow,transform,border-color,background-color] duration-200 ease-standard", false: "" },
  },
  compoundVariants: [
    {
      variant: "glow",
      interactive: true,
      className: "hover:border-brand/40 hover:shadow-card-hover motion-safe:hover:-translate-y-0.5 focus-within:border-brand/40",
    },
    { variant: "quiet", interactive: true, className: "hover:bg-surface-hover focus-within:bg-surface-hover" },
  ],
  defaultVariants: { variant: "glow", interactive: false },
})

function Card({ className, variant, interactive, ...props }: React.ComponentProps<"div"> & VariantProps<typeof cardVariants>) {
  return <div data-slot="card" data-variant={variant ?? "glow"} className={cn(cardVariants({ variant, interactive }), className)} {...props} />
}

function CardHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-header"
      className={cn("grid auto-rows-min grid-rows-[auto_auto] items-start gap-1.5 px-6 has-data-[slot=card-action]:grid-cols-[1fr_auto]", className)}
      {...props}
    />
  )
}

function CardTitle({ className, ...props }: React.ComponentProps<"h3">) {
  return <h3 data-slot="card-title" className={cn("font-heading text-lg leading-tight font-medium text-fg-heading", className)} {...props} />
}

function CardDescription({ className, ...props }: React.ComponentProps<"p">) {
  return <p data-slot="card-description" className={cn("text-sm font-normal text-fg-muted", className)} {...props} />
}

function CardAction({ className, ...props }: React.ComponentProps<"div">) {
  return <div data-slot="card-action" className={cn("col-start-2 row-span-2 row-start-1 self-start justify-self-end", className)} {...props} />
}

function CardMedia({ className, ...props }: React.ComponentProps<"div">) {
  // Nested radius: 12px media inside a 20px card with 8px inset.
  return <div data-slot="card-media" className={cn("mx-2 -mt-4 overflow-hidden rounded-sm", className)} {...props} />
}

function CardContent({ className, ...props }: React.ComponentProps<"div">) {
  return <div data-slot="card-content" className={cn("px-6", className)} {...props} />
}

function CardFooter({ className, ...props }: React.ComponentProps<"div">) {
  return <div data-slot="card-footer" className={cn("flex items-center gap-2 px-6", className)} {...props} />
}

export { Card, CardHeader, CardTitle, CardDescription, CardAction, CardMedia, CardContent, CardFooter, cardVariants }
