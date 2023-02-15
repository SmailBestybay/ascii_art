from PIL import Image
import operator
from functools import reduce
import sys

def average(pixel):
    return int(reduce(operator.add, pixel) / 3)

def min_max(pixel):
    return int((max(pixel) + min(pixel)) / 2)

def luminosity(pixel):
    return int( (0.21 * pixel[0]) + (0.72 * pixel[1]) + (0.07 * pixel[2]) )

modes = {'average' : average, 'min_max' : min_max, 'luminosity' : luminosity}

if len(sys.argv) == 0 or len(sys.argv) > 1:
    active_mode = modes['luminosity']
else:
    mode = sys.argv[1]
    if mode in modes:
        active_mode = modes[mode]
    else:
        active_mode = modes['luminosity']


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
        brightness_level = active_mode(im.getpixel((x,y)))
        symbol_index = int(len(symbols) * (brightness_level / 255)) - 1 
        im_array[y].append(symbols[symbol_index])

for row in range(len(im_array)):
    for col in range(len(im_array[row])):
        print(im_array[row][col], end='')
        print(im_array[row][col], end='')
    print()
