# for문과 if문을 이용해 과락 과목 출력하기

minScore = 60
scores = [
    ['국어', 87],
    ['수학', 46],
    ['영어', 99],
    ['과학', 34]]

# for item in scores:
#     if item[1] < minScore:
#          print('과락 과목: {}, 과목 점수: {}'.format(item[0], item[1])) # 각가가 리스트 안의 리스트에서 인덱스를 말하는것??

# for subject, score in scores:
#     if score < minScore:
#         print('과락 과목: {}, 과목 점수: {}'.format(subject, score))

for subject, score in scores: # continue 사용하기 -> 다시 위쪽으로 올라감
    if score >= minScore: continue
    print('과락 과목: {}, 과락 점수: {}'.format(subject, score))