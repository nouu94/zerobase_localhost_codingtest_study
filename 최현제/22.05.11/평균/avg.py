# 평균 : 평균을 구하자! 
# 여러 수나 양의 중간값을 갖는 수를 평균이라고 한다.

# import random

# nums = random.sample(range(0,100), 10)
# print(f'nums : {nums}')

# total = 0
# for n in nums : 
#     total += n

# avg = total / len(nums)
# print(f'avg : {round(avg)}')

# 50 이상 90 이하 수들의 평균 
# import random 

# nums = random.sample(range(0, 100), 30)
# print(f'nums : {nums}')

# target_nums = []
# total = 0
# # target = 0

# for n in nums : 
#     if n >= 50 and n <= 90 : 
#         total += n 
#         # target += 1
#         target_nums.append(n)

# average = total / len(target_nums)
# print(f'target_nums : {target_nums}')
# print(f'average : {round(average, 2)}')

# 정수들의 평균 
# nums = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.159, 1, 11, 12.789]
# print(f'{nums}')

# target_nums = []
# total = 0

# for n in nums : 
#     if n - int(n) == 0 : 
#         total += n
#         target_nums.append(n)

# print(f'total : {total}')
# print(f'target_nums : {target_nums}')


# 실수들의 평균 
nums = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.159, 1, 11, 12.789]
# print(f'{nums}')

target_nums = []
total = 0

for n in nums : 
    if n - int(n) != 0 : 
        total += n
        target_nums.append(n)

print(f'total : {total}')
print(f'target_nums : {target_nums}')