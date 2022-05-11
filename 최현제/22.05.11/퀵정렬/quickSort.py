# 1. 가운데 값을 먼저 비교
# 2. 가운데 값보다 더 큰 수를 오른쪽에 오름차순 정렬 몰아놓고 작은 수를 왼쪽에 오름차순 정렬로 몰아넣음 
# 3. 반복 

# 기준보다 작은 값과 큰 값을 분리한다. 퀵정렬 
# 8 1 4 3 2 5 4 10 6 8 

# 1 4 3 2 4     5     8 10 6 8 
# 전체 데이터를 다 봐서 작은 값들을 왼쪽에 위치, 큰 값들을 오른쪽에 위치

# 1 4   3   2 4 
# 1 2   3   4 4

# 8 10  6   8 
# 6     8 8 10

# 무언가 반복을 하기 떄문에 재귀 함수를 사용합니다. 

def qSort(ns) : 

    if len(ns) < 2 : 
        return ns 

    mid_idx = len(ns) // 2 #미드 인덱스
    mid_value = ns[mid_idx] # 미드 아이템


    small_nums = []; same_nums = []; big_nums = []

    for n in ns : 
        # 양분
        if n < mid_value :
            small_nums.append(n)
        elif n == mid_value :
            same_nums.append(n)
        else :
            big_nums.append(n) 


    return qSort(small_nums) + same_nums + qSort(big_nums) # 리스트 연결(concat)

nums = [8, 1, 4, 3, 2, 5, 4, 10, 6, 8]
print(f'qSort(nums) : {qSort(nums)}')



