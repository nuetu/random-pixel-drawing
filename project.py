from graphics import *
import random
import time
win = GraphWin()

###################
width = 25
height = width
pixelSize = 10
color_variety = 10
###################

###################
#initializations
rectangleArray = []
red = random.randint(0,255) 
green = random.randint(0,255)
blue = random.randint(0,255)
r = red
g = green
b = blue

###################

def createGrid(n,m):
    grid = n
    pixel = m
    x = 0
    y = 0
    w = pixel

    i = 1
    while i <= (grid*grid):
        pt = Point(x,y)
        y += pixel
        pt2 = Point(w,y)
        #rect = Rectangle(pt, pt2)
        #rect.draw(win)
        rectangleAppend = (pt,pt2)
        rectangleArray.append(rectangleAppend)
        if i % grid == 0:
            x += pixel
            y = 0
            w += pixel
        fastmath = (i/(grid*grid))*100
        #print("Loading... [", str(round(fastmath, 2)) ," / 100 ] ")
        i += 1


##################

createGrid(width, pixelSize) #width, pixel size
index = random.randrange(len(rectangleArray))
#print(index)
point1,point2 = rectangleArray[index]
invalidIndex = []

##################

def variety(x):
    num = random.randint(-1*color_variety,color_variety)
    if (x + num > 255 or x + num < 0):
        return -1 * num
    else: 
        return num

i = 0
while i <= len(rectangleArray) - 1:
    invalidIndex.append(i)
    i += 1
invalidIndex.remove(index)

def cardinal(x):
    validDirection = []
    up = x - 1 
    down = x + 1
    right = x + height
    left = x - height
    if (not(x % height == 0) and up >= 0 and up in invalidIndex):
        validDirection.append(up)
    if ((not(down % height == 0) and down < width * height - 1) and (down in invalidIndex)):
        validDirection.append(down)
    if ((right < width * height) and (right in invalidIndex)):
        validDirection.append(right)
    if ((left > 0) and (left in invalidIndex)):
        validDirection.append(left)
    if (len(validDirection) > 0):
        out = random.choice(validDirection)
    else: 
        out = random.choice(invalidIndex)
    return out 

def nextPixel():
    global invalidIndex, index, point1, point2
    index = cardinal(index)
    invalidIndex.remove(index)
    point1,point2 = rectangleArray[index]

i = 0
while i <= len(invalidIndex):
    rect = Rectangle(point1,point2)
    rect.setFill(color_rgb(r,g,b))
    rect.setOutline(color_rgb(r,g,b))
    rect.draw(win)
    r += variety(r)
    g += variety(g)
    b += variety(b)
    if (i != len(invalidIndex)):
        nextPixel()
    else:
        break 
