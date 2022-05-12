# 순위 알고리즘 
# 숫자로 이루어진 리스트에서 아이템의 순위를 출력하고, 순위에 따라 아이템을 
# 정렬하는 모듈을 만들어보자. 리스트는 50부터 100까지의 난수 20개를 이용하자. 

# nums : [85, 53, 91, 77, 56, 62, 80, 94, 83, 69, 75, 81, 61, 73, 57, 64, 74, 70, 86, 98]
# rank [4, 19 2, 8, 18, 15, 7, 1, 5, 13, 9, 6, 16, 11, 17, 14, 10, 12, 3, 0]
# sequence_nums : [98, 94, 91, 86, 85, 83, 81, 80, 77, 75, 74, 73, 70, 69, 64, 62, 61, 57, 56, 53]

import random
import rankMod

if __name__ == '__main__':

    nums = random.sample(range(50, 101), 20)
    sorted_nums = rankMod.rankAlgorithm(nums)
    print(f'sorted_nums : {sorted_nums}')



