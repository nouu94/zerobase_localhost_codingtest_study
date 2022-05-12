# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들어 보자. 
'''
1. 검색 모듈은 선형 검색 알고리즘을 이용하자.
2. 리스트는 1부터 20까지의 정수 중에서 난수 10개를 이용하자.
3. 검색 과정을 로그로 출력하자. 
4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없다면 -1을 출력하자. 
'''

import linearSearch
import random 

if __name__ == '__main__' :

    # 중복값 x
    r_nums = random.sample(range(1, 21), 10)
    search_num = int(input('input search number : '))

    result_idx = linearSearch.searchNumberByLinearAlgorithm(r_nums, search_num)

    if result_idx == -1 :
        print('No results found')
        print(f'search result index : {result_idx}')

    else : 
        print('>>> Search Results <<<')
        print(f'search result index : {result_idx}') 
        print(f'search result number : {r_nums[result_idx]}')

    


    