# 순위 : 어떠한 값에 랭크를 정하자!
# 수의 크고 작음을 이용해서 수의 순서를 정하는 것을 순위라고 한다. 

# 정렬이 되지 않는 자료구조 
# 순위 자료 구조 

import random 

# 50 ~ 100 사이 중 20개를 리스트 형태로 담는다.
lst = random.sample(range(50, 101), 20)

# lst 에 대한 순위를 지정하는 ranks 리스트를 하나 생성한다.
# list comprehension
ranks = [0 for _ in range(len(lst))]

print(f'lst : {lst}')
print(f'ranks : {ranks}')

for idx, num1 in enumerate(lst) : 
    # 하나씩 뒤로 가면서 다 비교해야한다
    for num2 in lst : # lst를 한번 더 순회
        if num1 < num2 : # 첫 for문에서 선언한 num1과 두번째 num2를 비교
            ranks[idx] += 1 # num1이 더 크다면 ranks 아이템 값을 1 증가

# print(f'lst : {lst}')
# print(f'ranks : {ranks}')

# for문을 통해 출력
for idx, num in enumerate(lst) : 
    print(f'lst : {num} \t {ranks[idx] + 1}')