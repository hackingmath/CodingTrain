'''After Shiffman's Coding Challenge #102
May 8, 2018
with Jared'''

#cols = 200
#rows = 200

current = []
previous = []

damping = 0.9

def setup():
    global rows, cols
    size(300,300)
    cols = width
    rows = height
    for i in range(cols):
        current.append([])
        previous.append([])
        for j in range(rows):
            current[i].append(100)
            previous[i].append(100)
    #previous[100][100] = 255
    
def mousePressed():
    #index = mouseX + mouseY*rows
    current[mouseX][mouseY] = 255
    
def draw():
    global current, previous,damping,rows,cols
    background(0)
    loadPixels()
    for i in range(1,cols-1):
        for j in range(1,rows-1):
            current[i][j] = (previous[i-1][j] + previous[i+1][j] + \
                             previous[i][j-1] + previous[i][j+1]) / 2 - \
                            previous[i][j]
            current[i][j] *= damping
            index = i + j*cols
            pixels[index] = color(current[i][j])
            
    updatePixels()
    previous,current = list(current),list(previous)