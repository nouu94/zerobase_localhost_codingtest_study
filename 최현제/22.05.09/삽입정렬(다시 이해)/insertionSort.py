# 삽입정렬 : 정렬 위치를 찾아 들어가자! 
# 삽입정렬은 버블정렬과 좀 반대의 개념 
# 이미 정렬되어 있는 부분에 나 자신이 어디에 들어가는지 판단해서 정렬을 하는 방식

'''
정렬되어 있는 자료 배열과 비교해서, 정렬 위치를 찾는다.
[(5, 10), 2, 1, 0] -> [2, 5, 10] 1회전
[(2, 5, 10), 1, 0] -> [1, 2, 5, 10] 2회전
[(1, 2, 5, 10), 0] -> [0, 1, 2, 5, 10] 3회전
[0, 1, 2, 5, 10]

정렬은 2번째 위치(index)의 값을 temp에 저장한다.
temp와 이전에 있는 원소들과 비교하며 삽입해나간다.
'1'번으로 돌아가 다음 위치(index)의 값을 temp에 저장하고, 반복한다
'''
# asc(오름차순)
nums = [5, 10, 2, 1, 0]

for idx1 in range(1, len(nums)) : 
    idx2 = idx1 - 1 
    c_num = nums[idx1] 

    while nums[idx2] > c_num and idx2 >= 0 : 
        nums[idx2 + 1] = nums[idx2] 
        idx2 -= 1

    nums[idx2 + 1] = c_num 

print(f'nums : {nums}')

# desc(내림차순)
nums = [0, 5, 2, 10, 1]

for idx1 in range(1, len(nums)) : 
    idx2 = idx1 - 1 
    c_num = nums[idx1] 

    while nums[idx2] < c_num and idx2 >= 0 : 
        nums[idx2 + 1] = nums[idx2] 
        idx2 -= 1

    nums[idx2 + 1] = c_num 

print(f'nums : {nums}')

# 삽입 정렬에 대해 다시 정리해야겠네.



