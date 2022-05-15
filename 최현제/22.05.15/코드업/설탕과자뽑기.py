h, w = map(int, input().split())

grid = [[0 for col in range(w)] for row in range(h)]
# print(grid)

n = int(input())

for _ in range(n) :
    l, d, x, y = map(int, input().split())

    
    for _ in range(l) :
        if d == 0 : 
            grid[x - 1][y - 1] = 1
            y += 1
        elif d == 1 : 
            grid[x - 1][y - 1] = 1
            x += 1

for x in range(h) : 
    for y in range(w) : 
        print(grid[x][y], end = ' ')
    print()
            

