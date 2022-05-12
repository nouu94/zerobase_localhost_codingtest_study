# 숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들어보자.
'''
1. 검색 모듈은 이진 검색 알고리즘을 이용하자.
2. 리스트는 [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]을 이용 
3. 검색 과정을 로그로 출력하자.
4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없다면 -1을 출력하자.
'''

import binarySearch

if __name__ == '__main__':
    nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
    search_num = int(input('input search number : '))

    # answer = binarySearch.solution(nums, 10)
    # print(f'answer : {answer}')

    result_idx = binarySearch.searchNumberByBinaryAlgorithm(nums, search_num)
    print(f'nums : {nums}')

    if result_idx == -1 : 
        print(f'no results found')
        print(f'search_result_idx : {result_idx}')

    else :
        print(f'>>> search Result <<<')
        print(f'>>> search Result index : {result_idx}')
        print(f'>>> search Result number : {nums[result_idx]}')

