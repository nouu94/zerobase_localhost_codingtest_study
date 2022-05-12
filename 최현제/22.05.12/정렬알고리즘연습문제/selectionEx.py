# 선택정렬 알고리즘 
# 선택정렬 알고리즘은 가장 작은 숫자 혹은 가장 큰 숫자를 찾아 자리 바꿈을 하는 알고리즘 
# 맨 앞 인덱스 값이 key 값이 되며, key값과 작은 숫자를 찾아 바꾼다 -> 다음 인덱스가 key값 작은 값으로 바꾼다.

import random 
import selectMod

if __name__ == "__main__":

    nums = random.sample(range(1, 21), 10)
    print(f'not sorted nums : \t{nums}')

    result = selectMod.sortSelectAlgorithm(nums)
    print(f'sorted nums by asc : {result}')

    result = selectMod.sortSelectAlgorithm(nums, asc = False)
    print(f'sorted nums by desc : {result}')


    


