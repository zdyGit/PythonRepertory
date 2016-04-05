import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

imageFile = "Wechat.png"
im  = Image.open(imageFile)
title = input()
#print(im.size)
font = ImageFont.truetype('方正中宋简体.ttf',24)

draw = ImageDraw.Draw(im)
draw.text((56,3),title,(226,90,117),font)
draw = ImageDraw.Draw(im)

im.show()