studentCnts  = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

sum = 0
avg = 0
n = 0
while n < len(studentCnts):
    classNo = studentCnts[n][0]
    cnt = studentCnts[n][1]
    print('{}학급의 학생수: {}명'.format(classNo, cnt))

    sum += cnt
    n += 1

print('전체 학생 수: {}'.format(sum))
print('평균 학생 수: {}'.format(sum / len(studentCnts)))

