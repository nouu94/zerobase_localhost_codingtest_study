'''
최빈값 알고리즘을 이용해서 학생 100명의 점수 분포를 다음과 같이 나타내 보자. 

1. 80 빈도수 : 28 +++++++++++++
2. 95 빈도수 : 22 +++++++++++
3. 90 빈도수 : 18 +++++++
4. 75 빈도수 : 13 ++++++
...
'''

import random 
import maxScore as ms

scores = []

for i in range(100) :

    rn = random.randint(71, 100)
    
    if rn != 100 :
        rn = rn - (rn % 5) 

    scores.append(rn)

print(f'scores : {scores}')
print(f'scores length : {len(scores)}')

# 최대값을 구해야 돼요.
max_alo = ms.MaxAlgorithm(scores)
max_alo.setMaxNumIdxAndNum()
max_num = max_alo.getMaxNum()

print(f'max_num : {max_num}')

# 인덱스 리스트 생성 
indexes = [0 for i in range(max_num + 1)]

# print(f'indexes : {indexes}')
# print(f'indexes : {len(indexes)}')

# 인덱스 리스트에 빈도 저장, 그리고 출력
for n in scores : 
    indexes[n] = indexes[n] + 1
print(f'indexes : {indexes}')

n = 1
while True : 

    max_alo = ms.MaxAlgorithm(indexes)
    max_alo.setMaxNumIdxAndNum()
    max_num = max_alo.getMaxNum()
    max_num_idx = max_alo.getMaxNumIdx()

    # print(f'max_num : {max_num}')
    # print(f'max_num_idx : {max_num_idx}')

    if max_num == 0 : 
        break

    print(f'{n}. {max_num_idx}빈도수 : {max_num}\t', end='')
    print('+' * max_num)

    indexes[max_num_idx] = 0

    n += 1

