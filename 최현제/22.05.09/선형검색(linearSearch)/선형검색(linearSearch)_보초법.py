# 보초법 : 마지막 인덱스에 찾으려는 값을 추가해서 찾는 과정을 간략화한다. 
# 인덱스 0부터 10까지 순차적으로 검색한다. 
# 검색 성공 : 마지막 이전 '9'가 검색된 경우, 검색 실패 : 마지막에 '9'가 검색된 경우

'''
ex 
datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4] 가 있고 선형 검색과 보초법을 이용하라.
만약 9를 찾고 싶다면 해당 리스트 끝에 9를 집어넣고, 있다면 len(datas) - 1 인덱스가 출력 될 것이고, 그렇지 않으면 9가 있는 임의의 인덱스가 출력 될 것이다.

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4, 9]
'''

datas = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas : {datas}') # [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas length : {len(datas)}') # 11

search_data = int(input('찾으려는 숫자 입력 : '))
search_result_idx = -1

datas.append(search_data) # 보초법, search_data 값을 맨 끝에 추가

n = 0 
while True : 

    if datas[n] == search_data : # 무한루프를 통해 datas의 값이 search_data와 같은지 순회 
        # 보초법, 만약 순회하는 인덱스 n이 datas의 맨 끝 값과 같지 않다면? 
        if n != len(datas) - 1 :
            search_result_idx = n # 순회되는 n 값 중 하나가 내가 찾는 값의 인덱스이다.
        break

    n += 1

print(f'datas : {datas}') # [3, 2, 5, 7, 9, 1, 0, 8, 6, 4, 88]
print(f'datas length : {len(datas)}') # 11
print(f'search_result_idx : {search_result_idx}') 

'''
이전 단순 선형 검색과 비교했을 때 
if n == len(datas) : 
        search_result_idx = -1
        break 

사라진 것을 볼 수 있다. 단순 선형 검색에서는 n == len(datas), if datas[n] == search_data 두 조건문을 이용하여 내가 찾으려는 값에 대한 어떠한 리스트 내 아이템이 있는지 없는지 판별 했다.


보초법을 통한 선형 검색은 내가 찾는 값을 리스트 끝에 할당한 뒤 무한 루프로 순회하며, 첫 if 조건문에는 if datas[n] == search_data를 통해 내가 찾는 값이 어디있는지 살피고, 중첩 if 문인 if search_data != len(datas) - 1 을 통해 내가 찾는 값이 datas 리스트의 맨 끝에 있는지 살핀다. 

!= 맨 끝에 있지 않다면 search_result_idx = n 으로 한다. 내가 찾으려는 값의 인덱스를 찾았으니 break!
'''


