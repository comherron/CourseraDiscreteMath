#print([[-1]*5]*5)
import copy
grid = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
deepGrid = copy.deepcopy(grid)
print(grid)

for i in grid:
    for j in i:
        j=0
print(grid)
i =0
j=0
while j < 1:
    i = 0
    while i < 5:
        grid[j][i] = 0
        i+= 1
    j+=1
    break
print(grid)
grid[2][3] = 5
print(grid)

print(deepGrid)

deepGrid[3][3]="Hello"
print(deepGrid)
