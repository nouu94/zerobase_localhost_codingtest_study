# 가장 작은 데이터를 찾아서 나와 위치를 바꾼다. 
# 선택정렬 알고리즘을 이용해서 학생 20명의 시험 점수를 오름차순과 내림차순으로 정렬하는 모듈을 만들어보자. 시험 점수는 50부터 100까지로 한다.

import random as rd
import sortMod as sm
import copy

scores = rd.sample(range(50, 101), 20)
# print(f'scores : {scores}')
# print(f'scores length : {len(scores)}')

result = sm.sortNumber(copy.deepcopy(scores))
print(f'result : {result}')
print(f'scores : {scores}')

result = sm.sortNumber(scores, asc = False)
print(f'result : {result}')