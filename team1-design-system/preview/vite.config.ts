import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import tailwindcss from "@tailwindcss/vite"
import { fileURLToPath } from "node:url"

const pkg = fileURLToPath(new URL("..", import.meta.url))

export default defineConfig({
  root: fileURLToPath(new URL(".", import.meta.url)),
  base: "./",
  plugins: [react(), tailwindcss()],
  resolve: { alias: { "@": pkg } },
  server: { fs: { allow: [fileURLToPath(new URL("../..", import.meta.url))] } },
  build: { emptyOutDir: true },
})
