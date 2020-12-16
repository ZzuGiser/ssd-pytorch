from road_ssd import SSD
from PIL import Image

ssd = SSD()

# img = input('Input image filename:')
img = "./road_images/3_13453_5563.jpg"

try:
    image = Image.open(img)
except:
    print('Open Error! Try again!')
else:
    r_image = ssd.detect_image(image)
    r_image.show()
