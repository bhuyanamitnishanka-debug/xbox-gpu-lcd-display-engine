# Xbox GPU LCD Display Engine

An end-to-end graphics and display architecture exploring the connection between 2D tile-map memory and compact LCD framebuffers, alongside modern console rendering pipelines.

## Project scope

- 2D tile-map memory at 256 x 256.
- LCD display framebuffers at 160 x 144.
- Rendering pipeline context for Microsoft Xbox Series X|S and Sony PlayStation 5.
- Related UI and 3D design workflows referencing Canva, Figma, and Adobe 3D.

## A note to future contributors

Dear future contributor,

You are welcome to contribute to this project, whatever your background or experience. Whether you have a code improvement, a documentation edit, an example, a test, a design idea, or a question, your input can help move it forward. For larger ideas, open an issue first so the direction can be discussed; for a small fix, a focused pull request with a short explanation is a great start. Please be respectful, explain any checks you ran, and be open to review feedback.

Thank you for helping this project grow.

To get started, [open an issue](https://github.com/bhuyanamitnishanka-debug/xbox-gpu-lcd-display-engine/issues/new) or [browse existing pull requests](https://github.com/bhuyanamitnishanka-debug/xbox-gpu-lcd-display-engine/pulls).

## Project website# Xbox GPU LCD Display Engine

An end-to-end graphics and display architecture exploring the connection between **2D tile-map memory (256×256)** and compact **LCD framebuffers (160×144)**, alongside modern console rendering pipelines (**Microsoft Xbox Series X|S** and **Sony PlayStation 5**) and UI/3D design workflows.

🌐 **Live Project Website:** [Visit the Xbox GPU LCD Display Engine Project Site](https://github.io)

---

## An Open Letter to GitHub Contributors

Dear Fellow Engineers, Graphics Programmers, Technical Artists, and Open-Source Builders,

Welcome to **`xbox-gpu-lcd-display-engine`**!

I started this repository with a clear conviction: the best way to master modern graphics hardware and console rendering pipelines is to understand how pixels are mapped, scrolled, layered, and pushed to a physical display from the ground up. Whether we are working with a classic `256×256` tile-map feeding a `160×144` LCD viewport or a modern **AMD RDNA** GPU executing **DirectX 12 Ultimate (HLSL)** and **PlayStation (GNM/PSSL)** compute shaders, the core principles of memory efficiency, viewport fitting, and layer priority remain timeless.

I warmly invite you to collaborate, experiment, and build alongside me in this repository:

* **Graphics & Shader Engineers:** Help optimize our **DirectX 12 HLSL** compute shaders (`src/lcd_compositor.hlsl`), expand support for **PSSL / Vulkan / WebGPU**, or benchmark rendering performance.
* **Python & Embedded Hardware Developers:** Improve the vectorized `NumPy` framebuffer compositor (`src/display_pipeline.py`), extend the **RGB565 SPI LCD hardware bridge** (`src/hardware_lcd_bridge.py`), or add real-time desktop/microcontroller display drivers.
* **UI/UX & 3D Pipeline Artists:** Contribute sample tile-maps, **Figma** HUD wireframes, **Canva** architectural diagrams, or **Unreal Engine 5 / Adobe 3D** integration guides.
* **First-Time Open-Source Contributors:** If you are looking for a welcoming repository to submit your first Pull Request, check our **Issues** and **Discussions** tabs—documentation improvements, unit tests, and interactive `index.html` enhancements are always appreciated.

Every contribution, code review, and architectural discussion makes this project stronger. Feel free to fork the repository, open an Issue, or say hello in **Discussion #1**.

Let's build clean, transparent, and inspiring graphics technology together.

Warm regards,  
**Amit Nishanka Bhuyan (`@bhuyanamitnishanka-debug`)**  
Project Maintainer, `xbox-gpu-lcd-display-engine`

---

## Project Scope

* **2D Tile-Map Memory:** `256 × 256` virtual tile canvas decoding `32 × 32` tile index grids (`8 × 8` pixel blocks) with wrap-around scrolling (`SCX`, `SCY`) and non-scrollable Window overlays (`WX`, `WY`).
* **Compact LCD Framebuffer:** `160 × 144` physical viewport fitting, layer priority arbitration (Background, Window, Object), and `RGBA8` / `RGB565` display output bridging.
* **Console Rendering Pipelines:** Hardware-software architectural context connecting classic display controllers with modern **Microsoft Xbox Series X|S** (**DirectX 12 Ultimate**, **HLSL**, **Xbox Velocity Architecture**) and **Sony PlayStation 5** (**GNM/GNMX**, **PSSL**, **Kraken SSD I/O**) pipelines.
* **UI & 3D Design Workflows:** End-to-end creative and engineering production stack referencing **Canva** (storyboards and concept decks), **Figma** (HUD/menu wireframes), **Adobe 3D** (**Substance 3D** PBR materials and **Photoshop**), and **Unreal Engine 5** (**C++**, **HLSL/PSSL**, **C#**, and **Python**).

---

## Repository Structure

```text
├── .github/
│   └── workflows/
│       └── pages.yml            # GitHub Actions workflow for automated GitHub Pages deployment
├── src/
│   ├── display_pipeline.py      # Python NumPy 256x256 to 160x144 framebuffer compositor
│   ├── lcd_compositor.hlsl      # DirectX 12 / Xbox-GPU compute shader
│   └── hardware_lcd_bridge.py   # Framebuffer-to-LCD RGB565 SPI & PPM output bridge
├── tests/
│   └── test_display_frame.py    # Unit tests for scrolling, window overlay, and priority rules
├── index.html                   # Interactive web showcase served via GitHub Pages
└── README.md
```

---

## Deployment (GitHub Pages)

* **Live URL:** `https://github.io`
* **Static Site Entry:** Served directly from `index.html` at the repository root.
* **Automated & Manual CI/CD:** The GitHub Actions workflow in `.github/workflows/pages.yml` automatically builds and deploys updates to **GitHub Pages** whenever changes are pushed to the `main` branch, and can also be triggered manually anytime via **`workflow_dispatch`** in the **Actions** tab.

---

## Quick Start

```bash
pip install numpy
python src/display_pipeline.py
```

---

## License

This project is open source and available under the **MIT License**.


Visit the [Xbox GPU LCD Display Engine project site](https://bhuyanamitnishanka-debug.github.io/xbox-gpu-lcd-display-engine/).

## Deployment

The static site is served from `index.html`. The workflow in `.github/workflows/pages.yml` deploys it to GitHub Pages when changes are pushed to `main`; it can also be started manually with `workflow_dispatch`.
