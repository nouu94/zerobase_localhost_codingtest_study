# 숫자로 이루어진 리스트를 병합정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈을 만들어보자.
# 단 정렬하는 과정도 출력하도록 한다. 

# 분할 단계 --> 병합 단계 

def mergeSort(ns, asc = True) : 

    if len(ns) < 2 :
        return ns

    # 병합정렬 알고리즘은 중간값(중간에 위치한 값)을 이용해서 자르고 자르고 분할시키고 다시 합침. 재귀 알고리즘 

    mid_idx = len(ns) // 2
    left_nums = mergeSort(ns[0: mid_idx], asc = asc)
    right_nums = mergeSort(ns[mid_idx: len(ns)], asc = asc)

    merged_nums = []
    left_idx = 0 ; right_idx = 0

    # 병합

    while left_idx < len(left_nums) and right_idx < len(right_nums) : 

        
        if asc : 
            if left_nums[left_idx] < right_nums[right_idx] : 
                merged_nums.append(left_nums[left_idx])
                left_idx += 1
            
            else : 
                merged_nums.append(right_nums[right_idx])
                right_idx += 1

        
        else :
            if left_nums[left_idx] > right_nums[right_idx] : 
                merged_nums.append(left_nums[left_idx])
                left_idx += 1
            
            else : 
                merged_nums.append(right_nums[right_idx])
                right_idx += 1

    merged_nums += left_nums[left_idx:]
    merged_nums += right_nums[right_idx:]

    # 재귀함수니까 단계별로 다 출력되겠죠잉?
    print(f'merged_nums : {merged_nums}')

    return merged_nums
