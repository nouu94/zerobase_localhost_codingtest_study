# 가족 이름을 리스트에 저장하고 출력해보자.

# myFamilyNames = ['홍아빠', '홍엄마', '홍길동', '홍동생']
# print(myFamilyNames)
# print(type(myFamilyNames))

# 오늘 일정을 리스트에 저장하고 출력해보자.

todaySchedule = ['10시-업무회의',
                 '12시-친구와의점심약속',
                 '3시-자료정리',
                 '6시-운동', '9시-TV시청']  #리스트 나열시 구분하기 쉽다
print(todaySchedule)
print(type(todaySchedule))

for todaySchedule in todaySchedule:
    print(todaySchedule) #앞에서 배운 for문을 활용한 일렬로 나열하기

#리스트 - 숫자, 문자, 논리형 모두 가능 + 리스트안에 또 다른 리스트도!