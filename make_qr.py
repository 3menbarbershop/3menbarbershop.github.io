"""Generate and verify the QR code: python3 make_qr.py https://USERNAME.github.io/3men/"""
import sys, segno, cv2

url = sys.argv[1]
if not url.startswith("https://"):
    sys.exit("URL must start with https://")

qr = segno.make(url, error="h")
qr.save("qr-3men.png", scale=20, border=4, dark="#0e0f12", light="#ffffff")
qr.save("qr-3men.svg", scale=10, border=4, dark="#0e0f12", light="#ffffff")

decoded, _, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread("qr-3men.png"))
print("encoded :", url)
print("decoded :", decoded)
print("MATCH" if decoded == url else "MISMATCH")
