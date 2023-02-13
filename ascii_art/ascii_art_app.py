from PIL import Image
im = Image.open("ascii_art/houses.jpeg")
print("Succesfully loaded image!")
print(f'Image size: {im.width} x {im.height}')

