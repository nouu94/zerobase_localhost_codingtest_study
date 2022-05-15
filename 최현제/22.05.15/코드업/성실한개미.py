# 2차원 배열 생성 및 할당
miro_box_lst = [[0 for col in range(10)] for row in range(10)]
x = 1
y = 1

for i in range(len(miro_box_lst)) :
    a = list(map(int, input().split())) # 리스트로 반환
    miro_box_lst[i] = a
# print(miro_box_lst)

while True : 
    if miro_box_lst[x][y] == 2 : # 먹이를 찾았을 때 종료
        miro_box_lst[x][y] = 9
        break
        
    elif miro_box_lst[x + 1][y] == 1 and miro_box_lst[x][y + 1] == 1 : # 가로와 아래가 막혔을 떄 종료
        miro_box_lst[x][y] = 9
        break
        
    miro_box_lst[x][y] = 9
    if miro_box_lst[x][y + 1] == 1 : # 오른쪽이 벽이면 아래로 1칸 
        x += 1
    elif miro_box_lst[x + 1][y] == 1 : # 아래쪽이 벽이면 오른쪽으로 1칸 
        y += 1
    else : # 주변에 벽이 없다면 우측으로 한칸 이동 miro_box_lst[x][y + 1] == 0 and miro_box_lst[x + 1][y] == 0
        y += 1

# print(miro_box_lst)
print('=================================================================')

for i in range(len(miro_box_lst)) : 
    for j in miro_box_lst[i] : 
        print(j, end=' ')
    print()