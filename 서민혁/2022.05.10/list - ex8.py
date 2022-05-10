minScore = 60

korScore = int(input('국어 점수: '))
engScore = int(input('영어 점수: '))
matScore = int(input('수학 점수: '))
sciScore = int(input('과학 점수: '))
hisScore = int(input('국사 점수: '))

scores = [
    ['국어', korScore],
    ['영어', engScore],
    ['수학', matScore],
    ['과학', sciScore],
    ['국사', hisScore],]

# for subject, score in scores:
#     if score < minScore:
#         print('과락 과목: {}, 과락 점수: {}'.format(subject, score))

n = 0
while n < len(scores):
    if scores[n][1] < minScore:
        print('과락 과목: {}, 점수: {}'.format(scores[n][0], scores[n][1]))

    n += 1
    continue
