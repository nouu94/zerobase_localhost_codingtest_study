import copy

def sortInsertAlgorithm(ns, asc = True) :
    copy_ns = copy.copy(ns)

    for i1 in range(1, len(copy_ns)) : 
        i2 = i1 - 1 # i1 보다 하나 앞에 있는 인덱스
        
        # 현재 정렬을 하려고 하는 아이템
        current_num = copy_ns[i1]

        if asc :
            while copy_ns[i2] > current_num and i2 >= 0 : 
                copy_ns[i2 + 1] = copy_ns[i2]
                i2 -= 1

        else :
            while copy_ns[i2] < current_num and i2 >= 0 : 
                copy_ns[i2 + 1] = copy_ns[i2]
                i2 -= 1

        copy_ns[i2 + 1] = current_num
        print(f'copy_ns : {copy_ns}')

    return copy_ns
    
     

    