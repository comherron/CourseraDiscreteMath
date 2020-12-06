
def makeGrid(size):
    ''' Takes an int Size that will be the size of a grid filled with -1
    returns the grid which is a double array'''
    grid = []
    for i in range(size):
        partOfGrid = []
        for j in range(size):
            partOfGrid.append(-1)
        grid.append(partOfGrid)
    return grid
test_grid =makeGrid(3)
assert test_grid == [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]], "makeGrid is no longer working"

def getZeros(grid):
    ''' Input:
    grid: a int[][] that represents the grid we are working on
    Output:
    an integer representing the number of zeros present in the grid
    Extra:
    terminates the moment it hits a -1 to save on run time (hopefully)'''
    total =0
    for i in grid:
        for j in i:
            if j ==0:
                total =total +1
            if j == -1:
                return total
    return total
assert getZeros([[0,0,0],[-1,-1,-1],[-1,-1,-1]]) == 3, "getZeros no longer works"

def getSlashes(grid):
    ''' Input:
    grid: a int[][] that represents the grid we are working on
    Output:
    an integer representing the number of slashes present in the grid
    Extra:
    terminates the moment it hits a -1 to save on run time (hopefully)'''
    total =0
    for i in grid:
        for j in i:
            if j == 2 or j == 1:
                total =total +1
            if j == -1:
                return total
    return total
assert getSlashes([[1,1,1],[2,0,-1],[-1,-1,-1]]) ==4, "getSlashes no longer works"

def resetGrid(grid,x,y):
    '''ResetGrid returns the grid modified back with -1
    but has the side effect of modifying the grid anyways so you can just run this
    and after x y is changed back to -1
    Purpose: is to fix modifications that occur when testing possible solutions
    Extra:
    Terminates upon encountering a -1 Assumes everything after is -1
    '''
    j = y
    i = x
    while j<len(grid):
        if(grid[j][i]==-1):
            break
        while i<len(grid[j]):
            grid[j][i]=-1
            i = i +1
        i=0
        j = j + 1
    return grid
test_grid =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print(resetGrid(test_grid,2,2))
assert resetGrid(test_grid,2,2) == [[1,2,3,4],[5,6,7,8],[9,10,-1,-1],[-1,-1,-1,-1]],"resetGrid doesnt work"

def extend_possible(grid,n,slash,x,y):
    '''Checks if it possible to continue if we were to add the given slash as x y'''
    if(slash==1):
        if x==0 and y==0:
            return True
        elif y==0:
            #1 check
            if grid[y][x-1]==2:
                return False
        elif x ==0:
            #2 Checks
            if grid[y-1][x]==2:
                return False
            elif grid[y-1][x+1]==1:
                return False
        elif x ==len(grid)-1:
            #2 checks
            if grid[y-1][x]==2:
                return False
            elif grid[y][x-1]==2:
                return False
        else:
            #3 checks
            if grid[y-1][x]==2:
                return False
            elif grid[y][x-1]==2:
                return False
            elif grid[y-1][x+1]==1:
                return False
        #will exit if statement and return true at the end
    elif(slash==2):
        if x==0 and y==0:
            return True
        elif y==0:
            #1 check
            if grid[y][x-1]==1:
                return False
        elif x ==0:
            #1 Checks
            if grid[y-1][x]==1:
                return False
        else:
            #3 checks
            if grid[y-1][x]==1:
                return False
            elif grid[y][x-1]==1:
                return False
            elif grid[y-1][x-1]==2:
                return False
    else: #it's a zero does it matter???
        if (getZeros(grid) +1)>(len(grid)*len(grid))-n:
            return False
    #grand catch all if nothing comes up false
    return True
test_grid = [[2,2,2],[1,1,-1],[-1,-1,-1]]
assert extend_possible(test_grid,6,1,0,0) ==True,"Problem with slash 1 first if"
assert extend_possible(test_grid,6,1,1,0) ==False,"Problem with slash 1 second if"
assert extend_possible(test_grid,6,1,0,1) ==False,"Problem with slash 1 third if"
assert extend_possible(test_grid,6,1,2,1) ==False,"Problem with slash 1 fourth if"
assert extend_possible(test_grid,6,1,1,1) ==False,"Problem with slash 1 else if"
#slash 2 assert checks
test_grid =[[1,1,1],[1,1,-1],[-1,-1,-1]]
assert extend_possible(test_grid,6,2,0,0) ==True,"Problem with slash 2 first if"
assert extend_possible(test_grid,6,2,1,0) ==False,"Problem with slash 2 second if"
assert extend_possible(test_grid,6,2,0,1) ==False,"Problem with slash 2 third if"
assert extend_possible(test_grid,6,2,1,1) ==False,"Problem with slash 2 fourth if"
#slash 0 assert checks
test_grid = [[0,0,0],[-1,-1,-1],[-1,-1,-1]]
assert extend_possible(test_grid,6,0,0,1) == False,"problem with slash 0 else case if"

def extend_helper(grid,n,x,y):
    '''Extend_helper
    Input: grid a int double array
    n the number of diagonals we want in the grid
    x the current x position in the array
    y the current y position in the array '''
    #debugging purposes
    if False:
        for i in grid:
            print(i)
        print("")
    size = len(grid)-1
    #we got the answer we were looking for
    if(getSlashes(grid)>=n):
        for i in grid:
            print(i)
        print("")
        exit()

    #index of out bounds
    if x > size or y >size:
        #print("index out of bounds")
        return
    #EXTENDING
    if extend_possible(grid,n,1,x,y):
        #print("EXTEND 1")
        grid[y][x] = 1
        if x==size:
            extend_helper(grid,n,0,y+1)
        else:
            extend_helper(grid,n,x+1,y)
        resetGrid(grid,x,y)
    if extend_possible(grid,n,2,x,y):
        #print("EXTEND 1")
        grid[y][x] = 2
        if x==size:
            extend_helper(grid,n,0,y+1)
        else:
            extend_helper(grid,n,x+1,y)
        resetGrid(grid,x,y)
    if extend_possible(grid,n,0,x,y):
        #print("EXTEND 1")
        grid[y][x] = 0
        if x==size:
            extend_helper(grid,n,0,y+1)
        else:
            extend_helper(grid,n,x+1,y)
        resetGrid(grid,x,y)


def extend(grid,n):
    '''wraper for extend function I found it easier to keep track of what part of the grid I am in
    by using parameters so that way I can move it recursively'''
    extend_helper(grid,n,0,0)
    if getSlashes(grid) < n:
        print("Did Not find answer")


extend(makeGrid(5),16)
