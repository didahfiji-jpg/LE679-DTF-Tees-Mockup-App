"""Generate a sharp, multi-resolution Windows icon for LE679 DTF Tees V1."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 1024
image = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(image)
d.rounded_rectangle((40, 40, 984, 984), radius=206, fill=(9, 14, 38, 255))
# Neon edge treatment and gradient-filled central plate
for i in range(18):
    t = i / 17
    color = (int(16 + 45*t), int(219 - 150*t), int(255 - 20*t), 255)
    d.rounded_rectangle((50+i*2, 50+i*2, 974-i*2, 974-i*2), radius=195-i, outline=color, width=3)
d.rounded_rectangle((115, 125, 909, 850), radius=116, fill=(12, 20, 57, 255), outline=(110, 45, 243, 255), width=14)
# Angular neon crest
d.polygon([(512, 165),(750, 294),(750, 492),(512, 623),(274, 492),(274, 294)], fill=(31, 29, 88, 255), outline=(40, 231, 255, 255), width=22)
d.line([(512, 165),(512, 623)], fill=(178, 72, 255, 255), width=14)
d.line([(274, 294),(512, 425),(750, 294)], fill=(73, 207, 255, 255), width=15)
fontpath = "C:/Windows/Fonts/arialbd.ttf"
font = ImageFont.truetype(fontpath, 170)
d.text((512, 395), "679", anchor="mm", font=font, fill=(255,255,255,255), stroke_width=6, stroke_fill=(5,10,40,255))
small = ImageFont.truetype(fontpath, 88)
d.text((512, 732), "DTF TEES", anchor="mm", font=small, fill=(255,255,255,255), stroke_width=3, stroke_fill=(15,20,50,255))
# Clear V1 tab, deliberately inset for safe Windows icon scaling
d.rounded_rectangle((704, 760, 928, 922), radius=44, fill=(25, 11, 59, 255), outline=(45, 229, 255, 255), width=14)
vfont = ImageFont.truetype(fontpath, 116)
d.text((816, 839), "V1", anchor="mm", font=vfont, fill=(255,255,255,255))
image.save("app-icon-1024.png", dpi=(300, 300))
image.save("app.ico", format="ICO", sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
print("Generated 1024px master (300 DPI metadata) and multi-size Windows ICO")
