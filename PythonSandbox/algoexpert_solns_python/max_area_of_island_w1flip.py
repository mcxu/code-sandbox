'''
Given 2d grid of 0's and 1's, with "islands" of 1's,
return the max area from flipping a cell from 0 to 1.
'''
def maxArea(grid):
    maxAreaSoFar = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            currVal = grid[y][x]
            areaFromCell = 0
            visited = set()
            if currVal == 0 and (y,x) not in visited:
                grid[y][x] = 1
                # do dfs
                areaFromCell = getArea(grid, y,x, visited)
                grid[y][x] = 0
            else:
                # do dfs
                areaFromCell = getArea(grid, y,x, visited)

            if areaFromCell > maxAreaSoFar:
                maxAreaSoFar = areaFromCell
    return maxAreaSoFar

def getArea(grid, y, x, visited):
    if y < 0 or y > len(grid)-1 or x < 0 or x > len(grid[0])-1:
        return 0
    if grid[y][x] == 0:
        visited.add((y,x))
        return 0
    
    if (y,x) not in visited:
        visited.add((y,x))
        up = getArea(grid, y-1, x, visited)
        down = getArea(grid, y+1, x, visited)
        left = getArea(grid, y, x-1, visited)
        right = getArea(grid, y, x+1, visited)
        return 1+up+down+left+right
    
    return 0

def test1():
    # grid = [
    #     [0,1,1,0,0],
    #     [1,0,0,0,1],
    #     [0,0,1,1,1]
    # ]
    grid = [
        [0,0,1,1,1],
        [1,0,1,1,1],
        [1,0,1,1,1]
    ]
    ma = maxArea(grid)
    print("max area: ", ma)
test1()