from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
CANVAS=(1080,1350); SAFE=64
def compose(scene_path, output_path, logo_path=None, headline="", support="", website="www.immigration.go.tz"):
    canvas=Image.open(scene_path).convert("RGB").resize(CANVAS,Image.Resampling.LANCZOS)
    draw=ImageDraw.Draw(canvas); font=ImageFont.load_default()
    if logo_path and Path(logo_path).exists():
        logo=Image.open(logo_path).convert("RGBA"); logo.thumbnail((150,150),Image.Resampling.LANCZOS)
        canvas.paste(logo,(CANVAS[0]-SAFE-logo.width,SAFE),logo)
    if headline: draw.text((SAFE,SAFE),headline,font=font,fill="white",stroke_width=2,stroke_fill="black")
    if support: draw.text((SAFE,150),support,font=font,fill="white",stroke_width=2,stroke_fill="black")
    draw.rectangle((0,1264,1080,1350),fill=(7,31,60))
    draw.text((SAFE,1295),"UHAMIAJI TANZANIA",font=font,fill="white")
    draw.text((750,1295),website,font=font,fill="white")
    Path(output_path).parent.mkdir(parents=True,exist_ok=True); canvas.save(output_path,"PNG")
