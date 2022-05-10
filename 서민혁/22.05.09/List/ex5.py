studentCnts = [[1, 19], [2, 21], [3, 22], [4, 19]]

for classNo, cnt in studentCnts: # 반복 가능한 객체이기 떄문에 바꿔줘서 간단하게
    print('{} 학급 학생의 수 : {}'.format(classNo, cnt))
