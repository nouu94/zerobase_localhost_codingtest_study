# 근삿값 : 가장 가까운 값을 찾자! 

# 특정 값 (참 값)에 가장 가까운 값을 근삿값이라고 한다. 
# [7, 43, 14, 44, 6, 26, 24, 3, 25, 47, 2, 32, 27, 38, 18, 17, 33, 29, 28, 0]
# input number : 11
'''
abs_num : 4 abs_num : 32 abs_num : 3 abs_num : 33 abs_num : 5
abs_num : 15 abs_num : 13 abs_num : 8 abs_num : 14 abs_num : 36
abs_num : 9 abs_num : 21 abs_num : 16 abs_num : 27 abs_num : 7
abs_num : 6 abs_num : 22 abs_num : 18 abs_num : 17 abs_num : 11
'''

import random 

nums = random.sample(range(0, 50), 20)
print(f'nums : {nums}')

input_num = int(input('input number : '))
print(f'input_num : {input_num}')

# 근삿값 코드 구문으로 구현 변수 두개와 
near_num = 0
min_num = 50

for n in nums : 
    abs_num = abs(n - input_num)
    # print(f'abs_num : {abs_num}')

    if abs_num < min_num :
        min_num = abs_num
        near_num = n

print(f'near_num : {near_num}')