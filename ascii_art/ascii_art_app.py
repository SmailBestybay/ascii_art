from PIL import Image
import operator
from functools import reduce

im = Image.open("ascii_art/houses.jpeg")
print("Succesfully loaded image!")
print(f'Image size: {im.width} x {im.height}')
resize_factor = 1
im = im.resize((im.width // resize_factor, im.height //  resize_factor))
print(f'Image new size: {im.width} x {im.height}')

symbols = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # 65 chars
im_array = []

for y in range(im.height):
    im_array.append([])
    for x in range(im.width):
        brightness_level = int(reduce(operator.add, im.getpixel((x,y)))/3)
        symbol_index = int(len(symbols) * (brightness_level / 255))
        im_array[y].append(symbols[symbol_index-1])

for row in range(len(im_array)):
    for col in range(len(im_array[row])):
        print(im_array[row][col], end='')
        print(im_array[row][col], end='')
    print()
