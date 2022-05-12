# def solution(nums, n) :
#     start = 0
#     mid = 0
#     end = len(nums) - 1

#     binary_search_idx = -1

#     while start <= end :

#         mid = (start + end) // 2

#         if n == nums[mid] :
#             binary_search_idx = mid
#             break

#         elif n > nums[mid] : 
#             start = mid + 1
        
#         elif n < nums[mid] : 
#             end = mid - 1

#     return binary_search_idx

def searchNumberByBinaryAlgorithm(ns, sn) : 

    search_result_idx = -1

    start_idx = 0
    end_idx = len(ns) -1
    mid_idx = (start_idx + end_idx) // 2
    mid_val = ns[mid_idx]

    print(f'start_idx : {start_idx}, end_idx : {end_idx}')
    print(f'mid_idx : {mid_idx}, mid_val : {mid_val}')

    while sn >= ns[0] and sn <= ns[len(ns) - 1] : 
        
        # 맨 마지막 숫자가 일치한 경우?
        if sn == ns[len(ns) - 1] : 
            search_result_idx = len(ns) - 1
            break
            
        if start_idx + 1 == end_idx : 
            if ns[start_idx] != sn and ns[end_idx] != sn :
                break

        if sn > mid_val :
            start_idx = mid_idx
            mid_idx = (start_idx + end_idx) // 2
            mid_val = ns[mid_idx]
            print(f'+start_idx : {start_idx}, end_idx : {end_idx}')
            print(f'+mid_idx : {mid_idx}, mid_val : {mid_val}')

        elif sn < mid_val : 
            end_idx = mid_idx
            mid_idx = (start_idx + end_idx) // 2
            mid_val = ns[mid_idx]
            print(f'-start_idx : {start_idx}, end_idx : {end_idx}')
            print(f'-mid_idx : {mid_idx}, mid_val : {mid_val}')

        elif sn == mid_val :
            search_result_idx = mid_idx
            break

    return search_result_idx


