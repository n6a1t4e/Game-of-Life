from random import *

width = 750
height = 750

def setup():
    size(width,height)
    frameRate(10)

res = width/100
rows = height/res
cols = width/res
    
newCells = [[0]*cols for i in range(rows)]
for i in range(len(newCells)):
    for j in range(len(newCells[i])):
        pick = randint(0,0)
        if pick == 0:
            newCells[i][j] = choice([0,1])

def draw():
    background(0)
    global newCells
    
    cells = newCells
    newCells = [[0]*cols for i in range(rows)]
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if cells[i][j] == 0:
                fill(255)
            else:
                fill(0)
            noStroke()
            rect(i*res, j*res, height/rows, width/cols)
    
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if i!=0 and j!=0 and i!=len(cells)-1 and j!=len(cells)-1:
                sum = 0
                for k in range(-1,2):
                    for l in range(-1,2):
                        sum += cells[i+k][j+l]
                sum -= cells[i][j]
                #print(sum)
                if cells[i][j] == 0:
                    if sum == 3:
                        newCells[i][j] = 1
                elif cells[i][j] == 1:
                    if sum <= 1 or sum >= 4: 
                        newCells[i][j] = 0
                    elif sum == 2 or sum == 3:
                        newCells[i][j] = 1
            else:
                newCells[i][j] = 0
    
    
