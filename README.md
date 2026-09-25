# Carousel Studio

Production-oriented carousel image pipeline for Tanzania Immigration public-education content.

## Core rule

**ONE SLIDE = ONE IMAGE FILE**

The system must never create:
- collages
- grids
- contact sheets
- split screens
- multi-panel compositions
- multiple slides inside one image
- slide numbers embedded into the artwork

Default output:
- 15 slides total
- Batch 1: 10 separate PNGs
- Batch 2: 5 separate PNGs
- 1080 × 1350 px
- 4:5 ratio

## Production goals

1. Plan carousel content from an article or narration.
2. Produce one prompt per slide.
3. Generate one background/scene image per slide.
4. Lock approved characters and uniform references.
5. Overlay official logo, typography, social icons and footer as deterministic assets.
6. Run QC before export.
7. Export each slide as a separate PNG.

See `SKILL.md` and `docs/ARCHITECTURE.md`.
