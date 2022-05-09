# 선택정렬 : 가장 작은 데이터를 찾아 자리 바꾸자!

# 주어진 리스트 중에 최소 값을 찾아, 그 값을 맨 앞에 위치한 값과 교체하는 방식으로 자료를 정렬하는 알고리즘이다.

# 주어진 리스트, 최소 값, 맨 앞에 위치한 값과 교체 

'''
[4, 2, 5, 1, 3]
[1, 2, 5, 4, 3]

[1, 2, 5, 4, 3]
[1, 2, 3, 4, 5]
'''

# 선택 정렬 오름차순 가정할 때 최소 값을 찾아 맨 앞에 위치한 값과 교체
# 중첩 for문을 통해 해결

nums = [4, 2, 5, 1, 3]
print(f'nums : {nums}')

for i in range(len(nums) - 1) : 
    min_idx = i # min_idx를 i로 선언

    for j in range(i + 1, len(nums)) : 
        if nums[min_idx] > nums[j] : 
            min_idx = j

    # temp_num = nums[i]
    # nums[i] = nums[min_idx]
    # nums[min_idx] = temp_num
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print(f'nums : {nums}')