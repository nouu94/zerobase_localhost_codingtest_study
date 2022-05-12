# 숫자로 이루어진 리스트를 삽입정렬 알고리즘을 이용해서 오름차순과 내림차순으로 
# 정렬하는 모듈을 만들어보자! (단 정렬하는 과정도 출력하도록 한다.)

# 삽입정렬 알고리즘은 무엇일까?
# 삽입정렬 오름차순 내림차순 
# 삽입정렬이라는건 이미 정렬되어 있는 숫자들 중 정렬되어 있는 숫자를 정하는 것 

# 앞에서부터 정렬. 버블정렬이네 상반되네 앞에서부터 정렬되는 것이니까! 
# 뒤쪽은 보지 않는 겁니다. 이미 정렬 되어 있는 데이터만 보고 거기서 내가 들어 갈 자리를 찾아서 들어간다. 

import random 
import insertMod

if __name__ == "__main__": 

    nums = random.sample(range(1, 21), 10)
    print('not sorted nums : \n{nums}')

    result = insertMod.sortInsertAlgorithm(nums)
    print(f'sorted nums by asc : \n{result}')

    result = insertMod.sortInsertAlgorithm(nums, asc = False)
    print(f'sorted nums by desc : \n{result}')    

