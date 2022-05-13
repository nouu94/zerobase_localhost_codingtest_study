# 다음은 회차별 로또 번호이다. 최빈도 알고리즘을 이용해서 모든 회차의 각각의 번호에 대한
# 빈도수를 출력하는 프로그램을 만들어보자.
import random 
import mod

lotto_nums = [[i for i in random.sample(range(1, 46), 6)] for _ in range(30)]
# print(lotto_nums)

lotto_mod = mod.LottoMod(lotto_nums)
m_list = lotto_mod.getLottoNumMod()

# print(f'm_list : {m_list}')
lotto_mod.printModList()


