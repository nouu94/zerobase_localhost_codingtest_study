# while문과 if문을 이용하여 과락 과목 출력하기

minScore  = 50
scores = [
    ['국어', 95],
    ['영어', 44],
    ['수학', 96],
    ['과학', 87],
    ['국사', 23],]

n = 0
while n < len(scores):
    if scores[n][1] < minScore:
        print('과락 과목: {}, 점수: {}'.format(scores[n][0], scores[n][1]))

    n += 1