# 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치(인덱스)와 검색 개수를 출력합시다.
# 함수라고 만들래서 만들었습니다. nums 파라미터는 리스트 형태이며, 인자로 리스트 형태의 데이터를 입력해야 합니다. 

def linearSearch(nums) :
    # nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]

    print(f'nums : {nums}')
    print(f'nums_length : {len(nums)}')

    search_num = int(input('찾을 값을 입력 : '))
    search_result_idxs = [] # 각각의 위치와 검색 갯수를 출력해야 하므로 search_result_idxs를 리스트 형태로 선언

    nums.append(search_num)

    n = 0

    # 함수의 모듈화 
    while True : 

        if nums[n] == search_num : 
            if n != len(nums) - 1 :
                search_result_idxs.append(n) # 얻고자 하는 값의 각각의 위치 인덱스를 추가

            else : break

        n += 1

    print(f'nums : {nums}')
    print(f'nums length : {len(nums)}')
    print(f'search_result_idxs : {search_result_idxs}')
    print(f'search_result_idxs_length : {len(search_result_idxs)}')


nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]
linearSearch(nums)

# 주의 할 점 : 보초법에 의해 끝에 있는 인덱스의 아이템은 세지 않는다. 
'''
search_result_idxs = -1로 선언했었지만 해당 문제는 각각의 위치(인덱스)와 
검색 개수를 출력 해야 한다. 따라서 search_result_idxs = []로 선언하여 
보초법에 근거한 여러 순환문과 조건문을 통해  그리고 search_result_idxs.append()로 찾을 값을 할당한다. 

마지막으로 print(f'search_result_idxs : {search_result_idxs}')을 출력하면 내가 찾을 값의 모든 인덱스 번호가 나올 것이며 print(f'search_result_idxs_length : {len(search_result_idxs)}')을 출력하면 내가 찾을 값이 해당 리스트 안에 몇개인지 알 수 있을 것이다.

'''