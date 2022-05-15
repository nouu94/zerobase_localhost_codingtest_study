grid = [[0 for col in range(19)] for row in range(19)]

for row in range(len(grid)) : 
    grid[row] = list(map(int, input('바둑알을 입력하세요(0은 흰 돌, 1은 검은 돌) : ').split()))

# print(grid)

n = int(input('십자 뒤집기 횟수를 입력하세요 : '))
for _ in range(n) : 
    x, y = map(int, input('십자 뒤집기 좌표를 입력하세요 x, y: ').split())
    
    for i in range(len(grid)) :
        # 세로 축에 대한 십자 뒤집기(각 행의 특정 원소들을 0이나 1로 전환)
        if grid[i][y - 1] == 0 : 
            grid[i][y - 1] = 1
        else : 
            grid[i][y - 1] = 0
    
        # 가로 축에 대한 십자 뒤집기(각 열의 특정 원소들을 0이나 1로 전환)
        if grid[x - 1][i] == 0 : 
            grid[x - 1][i] = 1
        else : 
            grid[x - 1][i] = 0


for row_idx, row in enumerate(grid) : 
    for col_idx, col in enumerate(grid[row_idx]) : 
        print(col, end = ' ')
    print()
        

        


        