# 가운데 데이터를 이용한다.
# 데이터가 정렬 되어 있어야한다.

# 리스트를 오름차순으로 정렬한 후 '7'을 검색하고 위치(인덱스)를 출력하자. 
nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]

nums.sort()

search_data = int(input('찾으려는 숫자 입력 : ')) # 내가 찾고자 하는 값
search_result_idx = -1 # 내가 출력하고자 하는 변수

start_idx = 0 
end_idx = len(nums) - 1
mid_idx = (start_idx + end_idx) // 2 
mid_value = nums[mid_idx]

while search_data <= nums[len(nums) - 1] and search_data > nums[0] :

    if search_data > mid_value : 
        start_idx = mid_idx
        mid_idx = (start_idx + end_idx) // 2
        mid_value = nums[mid_idx]

    elif search_data < mid_value :
        end_idx = mid_idx
        mid_idx = (start_idx + end_idx) // 2
        mid_value = nums[mid_idx]

    elif search_data == mid_value :
        search_result_idx = mid_idx
        break

print(f'search_result_idx : {search_result_idx}')

'''
혼자 한번 생각하면서 쳐 봣는데 

while search_data >= nums[len(nums) - 1] and search_data < nums[0] : 을 쳐서 내가 원하는 결과값이 나오지 않았다. 


다행히 vscode에 있는 디버깅 모드를 통해 하나 하나 살펴가면서 확인하여
while search_data <= nums[len(nums) - 1] and search_data > nums[0]로 해결하였다.
'''