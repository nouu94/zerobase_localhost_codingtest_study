def mSort(ns) : 

    if len(ns) < 2 : 
        return ns

    # 분할하는 단계
    mid_idx = len(ns) // 2
    left_nums = mSort(ns[0:mid_idx])
    right_nums = mSort(ns[mid_idx:len(ns)])

    merge_nums = []
    left_idx = 0; right_idx = 0

    # 병합하는 단계
    while left_idx < len(left_nums) and right_idx < len(right_nums) :

        if left_nums[left_idx] < right_nums[right_idx] :
            merge_nums.append(left_nums[left_idx])
            left_idx += 1

        else : 
            merge_nums.append(right_nums[right_idx])
            right_idx += 1

    merge_nums = merge_nums + left_nums[left_idx:]
    merge_nums = merge_nums + right_nums[right_idx:]

    return merge_nums


nums = [8, 1, 4, 3, 2, 5, 10, 6]
print(mSort(nums))
