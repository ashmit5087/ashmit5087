from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
import sys

src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("profile-photo.png")
out = Path("assets/ashmit-portrait.png")
img = Image.open(src).convert("RGB")
w,h = img.size
crop = img.crop((int(w*.28),int(h*.25),int(w*.82),int(h*.84)))
gray = ImageOps.grayscale(crop)
gray = ImageEnhance.Contrast(gray).enhance(1.45)
gray = ImageEnhance.Sharpness(gray).enhance(1.4)
out.parent.mkdir(parents=True, exist_ok=True)
gray.save(out, quality=95)
print(out)
