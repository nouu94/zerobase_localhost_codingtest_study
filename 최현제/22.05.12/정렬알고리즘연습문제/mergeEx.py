# 숫자로 이루어진 리스트를 병합정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈을 만들어보자.
# 단 정렬하는 과정도 출력하도록 한다. 

# 분할 단계 --> 병합 단계 분할 단계에서 

import mergeAlgorithm
import random 

r_nums = random.sample(range(1, 101), 10)
print(f'{r_nums}')
print(f'mergeAlgorithm.mergeSort(r_nums) : {mergeAlgorithm.mergeSort(r_nums)}')
# print(f'mergeAlgorithm.mergeSort(r_nums) : {mergeAlgorithm.mergeSort(r_nums, asc = False)}')