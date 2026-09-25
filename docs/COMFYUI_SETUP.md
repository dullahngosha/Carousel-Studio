# ComfyUI integration

Carousel Studio uses ComfyUI as a scene renderer, not as the authority for official graphic identity.

## Required template tags

Export a ComfyUI workflow in API format and rename node titles:
- CAROUSEL_POSITIVE
- CAROUSEL_NEGATIVE
- CAROUSEL_SEED
- CAROUSEL_SAVE

The adapter injects one slide prompt into one workflow execution. SaveImage must save one scene image for that job.

## Character reference conditioning

Install and configure one supported identity/reference method in ComfyUI, then wire approved Nyanzobe/Mbitiyaza images into that graph. The repository deliberately does not invent model filenames or node names because these vary by installed ComfyUI custom nodes.

## Production order

1. Run preflight.
2. Build 15 jobs.
3. Execute jobs 1-10 independently.
4. QC each output.
5. Composite locked official graphics.
6. Execute jobs 11-15 independently.
7. QC and export.

A failed slide is retried individually. Never combine failed slides into a sheet.
