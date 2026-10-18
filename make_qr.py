"""Generate and verify the 3MEN QR code.

Usage: python3 make_qr.py https://3menbarbershop.github.io/

Writes qr-3men.png (with the blue "3" in the centre) and qr-3men.svg (plain,
for print shops), then decodes the PNG again and checks it opens the same URL.
"""
import sys

import cv2
import segno
from PIL import Image, ImageDraw

url = sys.argv[1]
if not url.startswith("https://"):
    sys.exit("URL must start with https://")

DARK = "#0e0f12"
SCALE = 24
BORDER = 4

# Level H tolerates ~30 % damage, so the centre badge does not break scanning.
qr = segno.make(url, error="h", boost_error=False)
qr.save("qr-3men.svg", scale=10, border=BORDER, dark=DARK, light="#ffffff")
qr.save("qr-plain.png", scale=SCALE, border=BORDER, dark=DARK, light="#ffffff")

img = Image.open("qr-plain.png").convert("RGBA")
size = img.width
badge = int(size * 0.20)  # badge covers ~4 % of the area
icon = Image.open("icon.png").convert("RGBA").resize((badge, badge), Image.LANCZOS)
mask = Image.new("L", (badge, badge), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, badge - 1, badge - 1), radius=badge // 5, fill=255)
ring = badge + SCALE  # white quiet ring around the badge
plate = Image.new("RGBA", (ring, ring), (0, 0, 0, 0))
ImageDraw.Draw(plate).rounded_rectangle((0, 0, ring - 1, ring - 1), radius=ring // 5, fill="#ffffff")
img.alpha_composite(plate, ((size - ring) // 2, (size - ring) // 2))
img.paste(icon, ((size - badge) // 2, (size - badge) // 2), mask)
img.convert("RGB").save("qr-3men.png")

ok = True
for path in ("qr-3men.png", "qr-plain.png"):
    decoded, _, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread(path))
    print(f"{path}: decoded = {decoded!r}")
    ok &= decoded == url
print("encoded :", url)
print("MATCH" if ok else "MISMATCH")
sys.exit(0 if ok else 1)
