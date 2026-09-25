# Architecture

## 1. Planner

Converts article/narration into a strict ordered slide plan.

Each slide object contains:
- id
- headline
- support_text
- scene
- subjects
- location
- visual_goal
- source_notes
- image_prompt
- negative_prompt

## 2. Render Queue

Each slide becomes an independent render job.

Hard invariant:

`1 render job = 1 output image`

The queue rejects prompts containing instructions such as:
- collage
- grid
- contact sheet
- multi-panel
- multiple slides
- 2x2
- 3x3
- split screen

## 3. Reference Lock

Reference assets are registered in `config/project.yaml`.

Character references:
- Nyanzobe
- Mbitiyaza

Official assets:
- Immigration logo
- social icons
- approved uniform references

The image generator creates only the photographic/illustrative scene. Official graphic identity is composited afterward.

## 4. Compositor

Responsible for:
- official logo placement
- headline
- supporting copy
- footer
- social icons
- website
- safe margins

This prevents hallucinated logos and broken text.

## 5. QC

Checks:
- exact canvas 1080×1350
- one scene only
- no collage layout
- no slide number
- logo present from approved asset path
- footer present
- website exact
- text within safe margins
- character reference IDs match requested character
- dark navy uniform when officer is present

## 6. Batch exporter

For a 15-slide project:
- `batch-01/` contains slides 01–10
- `batch-02/` contains slides 11–15

Every slide is a separate PNG.
