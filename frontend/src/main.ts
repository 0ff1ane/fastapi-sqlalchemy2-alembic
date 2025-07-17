import { createInertiaApp, type ResolvedComponent } from "@inertiajs/svelte";
import { mount } from "svelte";
import "./app.css";
import Layout from "./layouts/Layout.svelte";

createInertiaApp({
  resolve: (name) => {
    const pages: Record<string, ResolvedComponent> = import.meta.glob(
      "./pages/**/*.svelte",
      { eager: true },
    );
    let page = pages[`./pages/${name}.svelte`];
    const layout = Layout as unknown as ResolvedComponent["layout"];
    return { default: page.default, layout };
  },
  setup({ el, App, props }) {
    if (el) {
      mount(App, { target: el, props });
    }
  },
});
