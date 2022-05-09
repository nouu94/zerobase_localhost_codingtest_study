# 가운데 데이터를 이용한다! 
# 중앙값을 이용한 검색 방법 입니다.
# 정렬되어 있다는 가정하에! 자료 구조에서 중앙값과의 크고 작음을 이용해서 데이터를 검색한다.
# min 값, 중앙값, max 값, 세 변수를 선언해야 이진 검색 코드 구문을 작성 할 수 있겠죠? 

'''
1, 2, 3, 4, 5, 6, 7, 8, 9
검색 대상 : 2, 2 < 5


1, 2, 3, 4, 5
검색 대상 : 2, 2 < 3

1, 2
검색 대상 : 2, 2 > 1
'''

# 정렬되어 있는 자료구조에서 중앙값과의 크고 작음을 이용해서 데이터를 검색한다. 

datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f'datas : {datas}')
print(f'datas length : {len(datas)}')

search_data = int(input('찾으려는 숫자 입력 : '))
search_result_idx = -1

# 이진 검색을 위한 시작 인덱스, 끝 인덱스, 가운데 인덱스, 가운데 값을 선언
start_idx = 0
end_idx = len(datas) - 1 # data 길이의 -1 만큼 뺴준다.
mid_idx = (start_idx + end_idx) // 2 # (start_idx + end_idx) // 2
mid_val = datas[mid_idx] # datas[mid_idx] 인덱싱을 통해 데이터 리스트의 가운데 값 선언 

# 이진 검색의 특성인 정렬 된 데이터가 있다는 가정을 하므로, 내가찾고자 하는 값이 데이터 리스트의 가장 큰값보다 작거나 같다 그리고 search_data가 데이터 리스트의 가장 작은 숫자보다 큰가? 라는 조건 연산자를 써서 반복문을 작성
while search_data <= datas[len(datas) - 1] and search_data > datas[0] :
    # 만약 내가찾고자 하는 값이 중앙 값보다 크다면?!
    if search_data > mid_val : 

        # 이진 검색의 특성에 의해 start_idx가 mid_idx가 됩니다. 또한 mid_idx가 (start_idx + end_idx) // 2, mid_val = datas[mid_val]을 재 정립합니다.
        start_idx = mid_idx
        mid_idx = (start_idx + end_idx) // 2
        mid_val = datas[mid_val]
        print(f'mid_idx : {mid_idx}')
        print(f'mid_val : {mid_val}')

    # 만약 내가 찾고자 하는 값이 중앙 값보다 작다면?! 
    elif search_data < mid_val : 

        # 이진 검색의 특성에 의해 end_idx가 mid_idx가 됩니다. 또한 mid_idx가 (start_idx + end_idx) // 2, mid_val = datas[mid_val]을 재 정립합니다.
        end_idx = mid_idx
        mid_idx = (start_idx + end_idx) // 2
        mid_val = datas[mid_idx]
        print(f'mid_idx : {mid_idx}')
        print(f'mid_val : {mid_val}')

    elif search_data == mid_val : 
        search_result_idx = mid_idx
        break

print(f'search_result_idx : {search_result_idx}')

'''
중앙값과의 크고 작음을 이용해서 데이터를 검색한다. 
그러기 위해서 start_idx, mid_idx, end_idx, mid_value를 선언한다. 

만약 내가 찾고자 하는 값 search_data > mid_val 이라면 start_idx가 mid_idx가 된다.
그렇지 않고 search_data < mid_val 이라면 end_idx가 mid_idx가 된다. 
그렇지 않고 search_data == mid_val 라면 search_data가 mid_val이 되므로 break!
'''


    

