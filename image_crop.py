import os
from PIL import Image

# The crop method takes four coordinates as input
# The right can represented as (left+width)
# lower can be represented ad (upper+height)

# OPEN A IMAGE
images_file = os.listdir('original image')


for image in images_file:
    print(image)
    filename, file_extension = os.path.splitext(image)
    image = os.path.join(r"C:\Users\Rana\Desktop\image resize\original image",image)

    im = Image.open(image)

    #original image width and height
    width, height = im.size
    print(width,height)

    im = im.crop((0, 0, 480, 480)) # left top right buttom

    file_path = os.path.join(r'C:\Users\Rana\Desktop\image resize\croped image', filename + "_resized"+ file_extension )


    im.save(file_path)


    






