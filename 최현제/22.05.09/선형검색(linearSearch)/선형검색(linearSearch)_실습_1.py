# 선형에서 데이터를 찾는다.

# 리스트에서 가장 앞에 있는 숫자 '7'을 검색하고 위치(인덱스)를 출력합시다.
nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]

print(f'nums : {nums}')
print(f'nums length : {len(nums)}')

search_data = int(input('input search number : '))
search_result_idx = -1

nums.append(search_data) # 보초법 구성 완료

n = 0
# 보초법에 대한 무한 루프 및 중첩 if문 구성 
while True : 

    if nums[n] == search_data : 
        if n != len(nums) - 1 : 
            search_result_idx = n
        break

    n += 1

print(f'nums : {nums}')
print(f'nums length : {len(nums)}')
print(f'search_result_idx : {search_result_idx}')

# 만약 search_result_idx가 0보다 작다면 -1이라는 뜻 이므로 해당 리스트의 아이템에 내가 찾고자 하는 값이 없는 것이다.
if search_result_idx < 0 : 
    print('not search index')
else :
    print('search index : {search_result_idx}')




# 리스트에서 숫자 '7'을 모두 검색하고 각각의 위치(인덱스)와 검색 개수를 출력합시다.