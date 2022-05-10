# 인덱스? 아이템에 부여되는 번호표
# 0부터~

#인덱스 짝수인 학생과 홀수인 학생을 구분해서 출력해보자

students = ['김성예', '신경도', '박기준', '최승철', '황동석']
# print('-- 인덱스가 짝수인 학생 --')
# print('students[0]: {}'.format(students[0]))
# print('students[2]: {}'.format(students[2]))
# print('students[4]: {}'.format(students[4]))
# print('-- 인덱스가 홀수인 학생 --')
# print('students[1]: {}'.format(students[1]))
# print('students[3]: {}'.format(students[3]))

for i in range(5):       #for문을 활용하여 간단하게 구별짓기
    if i % 2 == 0:
        print('인덱스가 짝수인 경우 ----> students[{}]: {}'.format(i, students[i]))
    else:
        print('인덱스가 홀수인 경우 ----> students[{}]: {}'.format(i, students[i]))

