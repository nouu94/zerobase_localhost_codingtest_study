# 배열 - 원소들을 순서대로 늘어놓은 것

# 예제
L = ['Bob', 'Cat', 'Spam', 'Programmers']
print(L[1])
print(L[-2])


# 1)원소 덧붙이기
L = ['Bob', 'Cat', 'Spam', 'Programmers']
L.append('New')

# 2)원소 꺼내기
L = ['Bob', 'Cat', 'Spam', 'Programmers', 'New']
L.pop() # ---> 끝에서 하나의 원소를 꺼냄

# 3)원소 삽입하기
L = [20, 37, 58, 72, 91]
L.insert(3, 65)  #-> L = [20, 37, 58, 65, 72, 91]

# 4)원소 삭제하기
L = [20, 37, 58, 65, 72, 91]
del(L[2]) # -> L = [20, 37, 65, 72, 91]

# 5)원소 탐색하기
L = ['Bob', 'Cat', 'Spam', 'Programmers', 'New']
L.index('Spam') # --> 2

# 순식간에 빠르게 할 수 있는 일 - > 리스트의 길이와 무관 (상수 시간) -> O(1) 라고 표시
# 리스트 길이가 길면 오래 걸리는 일 - > 리스트의 길이에 비례 (선형 시간) -> O(n) 라고 표시