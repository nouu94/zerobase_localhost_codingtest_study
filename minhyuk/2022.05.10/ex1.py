# while문을 이용하면 다양한 방법으로 아이템 조회가 가능하다.

studentCnts = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]

n = 0
while n < len(studentCnts):
    print('{}학급 학생수: {}'.format(studentCnts[n][0], studentCnts[n][1]))
    n += 1