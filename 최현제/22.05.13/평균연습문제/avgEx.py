# 다음은 어떤 체조선수의 경기 점수이다. 최댓값과 최솟값을 제외한 나머지 점수에 
# 대한 평균을 구하고 순위를 정하는 알고리즘을 만들어보자.

import maxAlgorithm, minAlgorithm
import nearAlgorithm

top5_scores = [9.12, 8.95, 8.12, 6.90, 6.18]
scores = [6.7, 5.9, 8.1, 7.9, 6.7, 7.3, 7.2, 8.2, 6.2, 5.8]
print(f'scores : {scores}')

max_a = maxAlgorithm.MaxAlgorithm(scores)
max_a.removeMaxScore()

min_a = minAlgorithm.MinAlgorithm(scores)
min_a.removeMinScore()

total = 0
average = 0

for n in scores :
    total += n

average = round(total / len(scores), 2)

print(f'total : {round(total, 2)}')
print(f'average : {average}')

tp = nearAlgorithm.Top5Players(top5_scores, average)
tp.setAlignScore()
top5Scores = tp.getFinalTop5Scores()
print(f'top5Scores : {top5Scores}')