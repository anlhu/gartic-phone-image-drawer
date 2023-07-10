import pyautogui, sys
import time
from PIL import Image
from collections import defaultdict

print('Place mouse in top left corner of drawing')
for i in range(7, 0, -1):
    print(i)
    time.sleep(1)
topLeft = pyautogui.position()
print(topLeft)

print('Place mouse at estimated lower right corner of drawing')
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
bottomRight = pyautogui.position()
print(bottomRight)

print('Place mouse on the custom color box')
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
customColor = pyautogui.position()
print(customColor)

print('Place mouse on the text box for "Red')
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
redBox = pyautogui.position()
print(redBox)

print('Place mouse on the text box for "Green')
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
greenBox = pyautogui.position()
print(greenBox)

print('Place mouse on the text box for "Blue')
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
blueBox = pyautogui.position()
print(blueBox)

img = Image.open("img.png")
img_width, img_height = img.size
img = list(img.getdata())

x_skip = 32
y_skip = 32
color_reduction = 16
width = bottomRight[0] - topLeft[0]
height = bottomRight[1] - topLeft[1]
color_to_pixels = defaultdict(list)
for x in range(topLeft[0], bottomRight[0], x_skip):
    for y in range(topLeft[1], bottomRight[1], y_skip):
        index = ((x-topLeft[0])*img_height//height) + ((y-topLeft[1])*img_height//height)*img_width
        color = img[index]
        newColor =tuple([int(color[i])//color_reduction * color_reduction for i in range(3)])
        img[index] = newColor
        color_to_pixels[newColor].append(index)

for i in range(5, 0, -1):
    print(f'starting in {i} seconds')
    time.sleep(1)

# TODO: go pixel by pixel through the drawing board and identify the corresponding pixel in the img array
#           add the RGB value through custom colors > double click and type each number > enter
#           draw the pixel with a click

for color in color_to_pixels:
    pyautogui.click(x=customColor[0], y=customColor[1])
    pyautogui.doubleClick(x=redBox[0], y=redBox[1])
    for i in str(color[0]):
        pyautogui.press(i)
    pyautogui.doubleClick(x=greenBox[0], y=greenBox[1])
    for i in str(color[1]):
        pyautogui.press(i)
    pyautogui.doubleClick(x=blueBox[0], y=blueBox[1])
    for i in str(color[2]):
        pyautogui.press(i)
    pyautogui.press('enter')
    index_list = color_to_pixels[color]
    for index in index_list:
        col = index % img_width
        row = index // img_width
        x = topLeft[0] + col/img_width*width
        y = topLeft[1] + row/img_height*height
        pyautogui.click(x=x, y=y)

# for x in range(topLeft[0], bottomRight[0], x_skip):
#     for y in range(topLeft[1], bottomRight[1], y_skip):
#         color = img[((x-topLeft[0])*img_height//height) + ((y-topLeft[1])*img_height//height)*img_width]
#         pyautogui.click(x=customColor[0], y=customColor[1])
#         pyautogui.doubleClick(x=redBox[0], y=redBox[1])
#         for i in str(color[0]):
#             pyautogui.press(i)
#         pyautogui.doubleClick(x=greenBox[0], y=greenBox[1])
#         for i in str(color[1]):
#             pyautogui.press(i)
#         pyautogui.doubleClick(x=blueBox[0], y=blueBox[1])
#         for i in str(color[2]):
#             pyautogui.press(i)
#         pyautogui.press('enter')
#         pyautogui.click(x=x, y=y)
