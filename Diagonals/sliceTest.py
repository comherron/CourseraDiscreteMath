grid = []
grid.extend([1,2,3,4,5])
print(grid)
x = grid[:]

x[2] = "test"
print("grid",grid)
print("X",x)


def test(ngrid):
    grid = ngrid[:]
    grid[0] = "empty"
print("Test with function")
print(grid)
test(grid)
print(grid)


GRID = [[1,2,3],[4,5,6],[7,8,9]]
def Clone(lis):
    return [i[:] for i in lis]
grid2 = Clone(GRID)

grid2[0][1] = "test"
print(GRID)
print(grid2)
