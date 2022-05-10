# 근삿값 알고리즘을 이용해서 시험 점수를 입력하면 학점이 출력되는 프로그램을 만들어보자.
# 평균 점수에 따른 학점 기준 점수는 다음과 같다.

import approximationClass as ac

scores = []

# 국어
kor = int(input('input kor score : '))
scores.append(kor)
# 영어
eng = int(input('input eng score : '))
scores.append(eng)
# 수학
mat = int(input('input mat score : '))
scores.append(mat)
# 과학
sci = int(input('input sci score : '))
scores.append(sci)
# 역사 
his = int(input('input his score : '))
scores.append(his)


total_score = sum(scores)
print(f'total_score : {total_score}')

avg_score = total_score / len(scores)
print(f'avg_score : {avg_score}')

grade = ac.getNearNum(avg_score)
print(f'grade : {grade}')