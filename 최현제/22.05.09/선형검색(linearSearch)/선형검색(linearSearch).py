# 선형에서 데이터를 찾는다.
# 선형으로 나열되어 있는 데이터를 순차적으로 스캔하면서 원하는 값을 찾습니다. 

# 인덱스 0부터 9까지 순차적으로 검색하는게 핵심입니다. (검색 성공 or 검색 실패)

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4] # 선형 검색을 하기 위한 데이터 리스트 생성 
print(f'datas : {datas}') # 데이타 리스트 출력 
print(f'datas length : {len(datas)}') # 데이터 리스트 길이 출력 10


search_data = int(input('찾으려는 숫자를 입력하세요 : ')) # 찾으려는 숫자 입력 
search_result_idx = -1 # 찾으려는 숫자의 인덱스 결과 값에 대한 변수 -1로 선언 

 
n = 0 # n은 임의의 인덱스를 가리킴.
# 무한 루프
while True : 

    # 순회되는 변수 n이 datas의 길이와 같다면
    if n == len(datas) : # 0 ~ 10 == 10
        search_result_idx = -1
        break 

    # 찾으려는 값이 데이터 리스트에 어떠한 위치에 있다면... 
    elif datas[n] == search_data : 
        search_result_idx = n
        break

    n += 1

print(f'search_result_idx : {search_result_idx}')

# 깨달은 점 #
'''
1. 결국 우리가 찾으려고 하는 것은 찾으려는 값의 인덱스이다. 인덱스를 찾기 위해 search_result_idx 변수를 일단 -1로 두었고 무한 루프 통해 찾으려는 값에 대한 인덱스를 구한다.

2. 선형 검색은 어떠한 리스트를 순차적으로 순회하여 우리가 목표로 하는 값의 인덱스를 찾는 것이다.
'''



