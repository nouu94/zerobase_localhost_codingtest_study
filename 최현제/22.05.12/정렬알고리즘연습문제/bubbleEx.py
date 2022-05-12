# 숫자로 이루어진 리스트를 버블 정렬 알고리즘을 이용해서 
# 오름차순과 내림차순으로 정렬하는 모듈을 만들어보자. (단 정렬하는 과정도 출력하도록 한다.)
# 하나씩 비교를 해서 큰 숫자를 뒤쪽으로 밀어내는 겁니다. 

# not sorted nums : [10, 4, 1, 13, 11, 16, 19, 14, 6, 5]

# sorted nums by ASC : [1, 4, 5, 6, 10, 11, 13, 14, 16, 19]
# sorted nums by DESC : [19, 16, 14, 13, 11, 10, 6, 5, 4, 1]

import random
import bubbleMod

if __name__ == '__main__':

    nums = random.sample(range(1, 21), 10)
    print(f'not sorted nums : {nums}')

    result = bubbleMod.sortBubbleAlgorithms(nums)
    print(f'sorted nums by asc: {result}')

    print()

    result = bubbleMod.sortBubbleAlgorithms(nums)
    print(f'sorted nums by desc: {result}')


