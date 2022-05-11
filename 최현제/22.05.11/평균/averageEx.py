import near 


# 특정 선수의 평균을 계산하고 삽입하기 전 
scores = [8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7]
top5PlayerScores = [9.12, 8.95, 8.12, 7.90, 7.88]
print(f'top5PlayerScores : {top5PlayerScores}')

total = 0; average = 0
for n in scores : 
    total += n

average = round(total / len(scores), 2)

print(f'total : {total}')
print(f'average : {average}')


tp = near.top5Players(top5PlayerScores, average)
tp.setAlignScore()
top5PlayerScores = tp.getFinalTop5Scores()
print(f'top5PlayerScores : {top5PlayerScores}')




