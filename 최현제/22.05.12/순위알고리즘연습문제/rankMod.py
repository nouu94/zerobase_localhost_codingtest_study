def rankAlgorithm(ns) : 
    
    ranks = [0 for i in range(len(ns))]

    for idx, n1 in enumerate(ns) : 

        for n2 in ns : # 나와 모든 아이템들을 다 비교하기위해 중첩반복문 사용
            if n1 < n2 : # 만약 나의 값이 또 다른 값보다 작다면 내가 속한 부분에 랭크 값을 1 증가
                ranks[idx] += 1

    print(f'nums : {ns}')
    print(f'ranks : {ranks}')


    for i, n in enumerate(ns) :
        print(f'num : {n} \t rank: {ranks[i] + 1}')

    sorted_nums = [0 for n in range(len(ns))]

    for idx, rank in enumerate(ranks) : 
        sorted_nums[rank] = ns[idx]


    return sorted_nums