# Production Workflow

First-time: install/start ComfyUI, run `scripts\setup_windows.bat`, add exact approved assets, and export a working API-format workflow to `workflows/scene-api.json`.

Every carousel: prepare factual narration, make exactly 15 ordered briefs, run preflight, dry-run, render 15 independent scenes, composite branding, run QC, visually inspect, export 10 separate PNGs then 5 separate PNGs.

```bat
scripts\preflight_windows.bat plans\geita.json
scripts\render_windows.bat plans\geita.json --dry-run
scripts\render_windows.bat plans\geita.json
```

Missing official assets must stop production rather than trigger substitutes.
