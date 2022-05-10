students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
sLength = len(students)

# for i in range(len(students)):  # len함수 써서 list길이가 엄청 길때도 쉽게 구현할 수 있다
#     print(students[i])

n = 0
while n < sLength:
    print('n : {}'.format(n))
    print('students[{}] : {}'.format(n, students[n]))
    n += 1  # while문을 통해 slength만큼 list를 반복함


str = 'Hello Python!!'
print('\'Hello Python!!\'의 길이 : {}'.format(len(str)))
