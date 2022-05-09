# 버블정렬 : 처음 부터 끝까지 차례로 비교하자!

'''
새 학년이 되어 학급에 20명의 새로운 학생들이 모였다. 학생들을 키 순서로 줄 세워 보자. 학생들의 키는 random 모듈, copy 모듈을 이용해서 170 ~ 185 사이로 생성한다. 
'''

import random as rd
import sortMod as sm
import copy


# rd.sample -> rd.randint로 바꿈 중복가능한 개체를 만들어야 되니까
students = []

for i in range(20) : 
    students.append(rd.randint(170, 185))

# print(f'students : {students}')

sorted_students = sm.bubbleSort(students, deepCopy = False)


# 약한 복사로 인해 두 변수가 같은 메모리를 가리킴
print(f'students : {students}')
print(f'sorted_students : {sorted_students}')


'''
깊은 복사와 약한 복사의 차이점과 어떻게 사용하는지 알아야 겠네요.
'''


