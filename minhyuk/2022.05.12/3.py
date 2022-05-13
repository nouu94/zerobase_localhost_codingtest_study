# L : 임의의 리스트
# x : int
'''''
def solution(lst, x):

    answer = lst[:]

    if answer[0] > x:
        answer.insert(0,x)

        return answer

    if answer[-1] < x:
        answer.append(x)

        return answer

    for idx in range(len(answer)):

        if answer[idx] < x and answer[idx + 1] > x:
            answer.insert(idx + 1, x)
            break

    return answer
''''

def solution(L, x):

    for idx, num in enumerate(L):
        if num > x:
            L.insert(idx,x)
            break

        if L[-1] < x:
            L.append(x)
        else:
            pass

    return L

