
from PIL import Image

with open("/home/phecda/VsCode/Information-Security/OpensslLab/recovered.raw", "rb") as f:
    data = f.read()

data = data[:432 * 475]

img = Image.frombytes("L", (432, 475), data)
img.save("recovered.png")
