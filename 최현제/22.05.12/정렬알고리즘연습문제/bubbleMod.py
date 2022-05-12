# 숫자로 이루어진 리스트를 버블 정렬 알고리즘을 이용해서 
# 오름차순과 내림차순으로 정렬하는 모듈을 만들어보자. (단 정렬하는 과정도 출력하도록 한다.)
# 하나씩 비교를 해서 큰 숫자를 뒤쪽으로 밀어내는 겁니다. 

# not sorted nums : [10, 4, 1, 13, 11, 16, 19, 14, 6, 5]

# sorted nums by ASC : [1, 4, 5, 6, 10, 11, 13, 14, 16, 19]
# sorted nums by DESC : [19, 16, 14, 13, 11, 10, 6, 5, 4, 1]

import copy 

def sortBubbleAlgorithms(ns, asc = True) :

    copy_ns = copy.copy(ns)

    length = len(copy_ns) - 1 # 전체 길이 - 1 인덱스 최대 크기

    for i in range(length) : 
        for j in range(length - i):

            if asc :
                if copy_ns[j] > copy_ns[j + 1] :
                    copy_ns[j], copy_ns[j + 1] = copy_ns[j + 1], copy_ns[j]

            else :
                if copy_ns[j] < copy_ns[j + 1] :
                    copy_ns[j], copy_ns[j + 1] = copy_ns[j + 1], copy_ns[j]

            print(f'ns : {copy_ns}') # 한번 회전 했을 때의 절차를 프린트
        print(f'{i + 1}회전 끝', end='\n\n')

    return copy_ns

            


