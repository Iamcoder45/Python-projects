import qrcode as qr
from datetime import datetime

img=qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")

img.save(f"ws_cube_{datetime.now()}.png")