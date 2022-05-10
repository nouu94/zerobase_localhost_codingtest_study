#자료구조 - 컨테이너 자료형, 리스트, 튜플, 딕셔너리, 셋트
#리스트 - 나열
#튜플 - 교체불가
#딕셔너리 - Key:value
#셋트 - 중복불가


student1 = '홍길동'
student2 = '박찬호'
student3 = '이용규'
student4 = '박승철'
student5 = '김지은'

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
print(students)
print(type(students))

for student in students:
    print(student)  #for문을 활용하여 데이터 하나하나 출력하기 - 리스트뿐만 아니고 튜플도 가능


# students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
# print(students)
# print(type(students))
#
# scores = {'kor': 95, 'eng': 98, 'mat': 100}
# print(scores)
# print(type(scores))
#
# allsales = {100, 200, 400, 200}
# print(allsales)
# print(type(allsales))