import { clsx, type ClassValue } from "clsx"
import { extendTailwindMerge } from "tailwind-merge"

// Team1 radius scale is xs / sm / lg / full; teach tailwind-merge the custom shadow + colour names.
const twMerge = extendTailwindMerge({
  extend: {
    theme: {
      radius: ["xs", "sm", "lg"],
      shadow: ["card", "card-hover", "button-hover", "overlay"],
    },
  },
})

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
