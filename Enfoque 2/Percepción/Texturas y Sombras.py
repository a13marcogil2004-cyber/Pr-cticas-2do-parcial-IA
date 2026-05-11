import numpy as np
from PIL import Image

img = Image.open("textura.jpg")
texture = np.array(img)

print(texture.shape)