# Xbox GPU LCD Display Engine

An end-to-end graphics and display architecture exploring the connection between 2D tile-map memory and compact LCD framebuffers, alongside modern console rendering pipelines.

## Project scope

- 2D tile-map memory at 256 x 256.
- LCD display framebuffers at 160 x 144.
- Rendering pipeline context for Microsoft Xbox Series X|S and Sony PlayStation 5.
- Related UI and 3D design workflows referencing Canva, Figma, and Adobe 3D.

## Project website

Visit the [Xbox GPU LCD Display Engine project site](https://bhuyanamitnishanka-debug.github.io/xbox-gpu-lcd-display-engine/).

## Deployment

The static site is served from `index.html`. The workflow in `.github/workflows/pages.yml` deploys it to GitHub Pages when changes are pushed to `main`; it can also be started manually with `workflow_dispatch`.
