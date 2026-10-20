
from PIL import Image
from collections import Counter

with open("/home/phecda/VsCode/Information-Security/OpensslLab/classified.enc", "rb") as f:
    data = f.read()

ciphertext = data[16:]

blocks = [
    ciphertext[i:i + 16]
    for i in range(0, len(ciphertext), 16)
]

counts = Counter(blocks)

shades = {
    block: int(i * 255 / max(len(counts) - 1, 1))
    for i, block in enumerate(counts)
}

pixels = bytearray()

for block in blocks:
    pixels.extend([shades[block]] * len(block))

pixels = pixels[:432 * 475]

img = Image.frombytes("L", (432, 475), bytes(pixels))
img.save("pattern_ecb.png")
