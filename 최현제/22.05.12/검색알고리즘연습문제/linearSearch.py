'''
ns : 랜덤 리스트 
sn : 찾으려는 값
'''

def searchNumberByLinearAlgorithm(ns, sn) :

    search_result_index = -1

    print(f'Numbers : {ns}')
    print(f'Search Numbers : {sn}')

    n = 0
    while True : 

        if n == len(ns) : 
            print('Search FAIL!!')
            break

        n += 1

        if ns[n] == sn :
            search_result_index = n
            print('search SUCCESS!!')
            print(f'search result INDEX!! : {search_result_index}')
            break

        
        n += 1

    return search_result_index

