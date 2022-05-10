# 좋아하는 운동 종목을 리스트에 저장하고 반복문을 이용하여 출력

myFavoriteSports = ['수영', '축구', '배구', '조깅', '야구']

# for i in range(len(myFavoriteSports)):  # i는 index
#     print('myFavoriteSports[{}] : {}'.format(i, myFavoriteSports[i])) # for문을 통해서 해당 list 출력

sLength = len(myFavoriteSports)

n = 0
while n < sLength:
    print('n : {}'.format(n))
    print('myFavoriteSports[{}] : {}'.format(n, myFavoriteSports[n]))
    n += 1  # while 반복문을 활용하여 List에 추가된 구성요소까지 출력

