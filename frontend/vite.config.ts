import { fileURLToPath } from "node:url";
import { defineConfig } from "vite";
import { dirname } from "path";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import tailwindcss from "@tailwindcss/vite";

const projectRoot = dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  plugins: [svelte(), tailwindcss()],
  resolve: {
    alias: {
      "@": `${projectRoot}/src`,
    },
  },
  build: {
    manifest: "manifest.json",
    outDir: "dist",
    rollupOptions: {
      input: "src/main.ts",
    },
  },
});
