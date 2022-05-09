# 버블정렬 : 처음 부터 끝까지 차례로 비교하자!

'''
새 학년이 되어 학급에 20명의 새로운 학생들이 모였다. 학생들을 키 순서로 줄 세워 보자. 학생들의 키는 random 모듈, copy 모듈을 이용해서 170 ~ 185 사이로 생성한다. 
'''
import copy

# ns : nums 라는 뜻
def bubbleSort(ns, deepCopy = True) : 
    
    if deepCopy : 
        # 새로운 메모리에 모습이 똑같은 ns 개체를 하나 생성했다고 볼 수 있다. 해당 변수 이름은 cns
        cns = copy.copy(ns)
    else :
        cns = ns

    length = len(cns) - 1

    # i는 버블 정렬 회전 수 
    for i in range(length) :
        # 버블 정렬의 성질에 입각해 length - i 만큼 빼면 됨
        for j in range(length - i) : 
            # 상대적으로 이전 인덱스에 있는 아이템이 다음 인덱스 아이템보다 크다면?
            if cns[j] > cns[j + 1] : 
                # 위치 변경!
                cns[j], cns[j + 1] = cns[j + 1], cns[j]


    return cns

