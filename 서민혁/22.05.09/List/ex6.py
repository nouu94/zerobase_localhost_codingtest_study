# 아래 표와 리스트를 활용하여 학급별 학생수, 전체 학생수, 평균 학생수 구하기

studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
sum = 0
avg = 0  # sum. avg 변수 정해주기
for classNo, cnt in studentCnts:
    print('{}학급 학생수: {}'.format(classNo, cnt))
    sum += cnt   # cnt 모두 더해주기

print('전체 학생수: {}'.format(sum))
print('평균 학생수: {}'.format(sum / len(studentCnts)))