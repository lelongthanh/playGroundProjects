from PIL import Image, ImageFilter

img = Image.open('./planet.jpg')
img.thumbnail((400,200))
img.save('thumbnail.jpg')

print(img.size)
