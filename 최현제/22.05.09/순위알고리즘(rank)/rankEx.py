import rankMod as rm
import random 

mid_stu_scos = random.sample(range(50, 101), 20)

end_stu_scos = random.sample(range(50, 101), 20)

rd = rm.RankDeviation(mid_stu_scos, end_stu_scos)
rd.setMidRank()
print(f'mid_stu_scos : {mid_stu_scos}')
print(f'mid_rank : {rd.getMidRank()}')


rd.setEndRank()
print(f'end_stu_scos : {end_stu_scos}')
print(f'end_rank : {rd.getEndRank()}')

rd.printRanksDeviation()

'''
클래스로 만들어서 기능을 모듈화하여 구현하려니 머리가 아픔
'''