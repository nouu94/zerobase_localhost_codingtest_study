# L : 리스트
# x : 정수
'''
L = [64, 72, 83, 72, 54]
x = 72
answer = [1, 3]

L = [64, 72, 83, 72, 54]
x = 83
answer = [2]

L = [64, 72, 83, 72, 54]
x = 49
answer = [-1]
'''


# def solution(L, x):
#     lst = L
#     answer = []

#     for i in range(len(lst)) :

#         if x == lst[i] :
#             answer.append(lst.index(x))
#             lst[lst.index(x)] = 0

#     if not answer :
#         answer.append(-1)

#     return answer

def solution(L, x):
    if x in L:
        answer = [i for i, y in enumerate(L) if y == x]

    else:
        answer = [-1]

    return answer