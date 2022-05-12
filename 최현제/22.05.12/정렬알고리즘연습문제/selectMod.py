import copy

def sortSelectAlgorithm(nums, asc = True) : 
    
    copy_nums = copy.copy(nums)

    for i in range(len(copy_nums) - 1) : 
        min_idx = i # 가장 작은 인덱스 선언 

        for j in range(i + 1, len(copy_nums)) : 
            # 작은 값이 있는 인덱스를 찾는 순환 코드
            if asc :
                if copy_nums[min_idx] > copy_nums[j] : 
                    min_idx = j
            else :
                if copy_nums[min_idx] < copy_nums[j] : 
                    min_idx = j
            
        
        copy_nums[i], copy_nums[min_idx] = copy_nums[min_idx], copy_nums[i]
        print(f'nums : {copy_nums}')

    return copy_nums


    
    