# 학생수 가장 적은 학급과 가장 많은 학급을 출력해보자

studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]


minClassNo, minCnt = studentCnts[0]
maxClassNo, maxCnt = studentCnts[0]

for classNo, cnt in studentCnts:
    if cnt < minCnt:
        minClassNo = classNo
        minCnt = cnt
        print('가장 적은 학급(학생수): {}학급({}명)'.format(minClassNo, minCnt))

    if cnt > maxCnt:
        maxClassNo = classNo
        maxCnt = cnt
        print('가장 많은 학급(학생수): {}학급({}명)'.format(maxClassNo, maxCnt))

#for문 사용

# studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
#
# minClassNo = 0; maxClassNo = 0
# minCnt = 0; maxCnt = 0
#
# for classNo, cnt in studentCnts:
#     if minCnt == 0 or minCnt > cnt:
#         minClassNo = classNo
#         minCnt = cnt
#     if maxCnt < cnt:
#         maxClassNo = classNo
#         maxCnt = cnt
# print('학생 수가 가장 적은 반 (학생 수) : {} 반( {} 명)'.format(minClassNo, minCnt))
# print('학생 수가 가장 많은 반 (학생 수) : {} 반( {} 명)'.format(maxClassNo, maxCnt))