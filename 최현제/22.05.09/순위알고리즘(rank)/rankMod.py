# 랭크 편차 클래스 생성
class RankDeviation : 

    # mss는 중간고사 리스트, ess는 기말고사 리스트
    def __init__(self, mss, ess) :

        self.mid_stu_scos = mss
        self.mid_ranks = [0 for _ in range(len(self.mid_stu_scos))]

        self.end_stu_scos = ess
        self.end_ranks = [0 for _ in range(len(self.end_stu_scos))]

        self.rank_deviation = [0 for _ in range(len(self.end_stu_scos))]
    

    # ss는 점수, rs는 랭크(순위) - 중간고사, 기말고사의 순위 산출
    def setRank(self, ss, rs) :
        for idx, sco1 in enumerate(ss) : 
            for sco2 in ss :
                if sco1 < sco2 : 
                    rs[idx] += 1


    def setMidRank(self) : 
        self.setRank(self.mid_stu_scos, self.mid_ranks)

    def getMidRank(self) : 
        return self.mid_ranks




    def setEndRank(self) : 
        self.setRank(self.end_stu_scos, self.end_ranks)

    def getEndRank(self) : 
        return self.end_ranks


    def printRanksDeviation(self) : 

        for idx, mRank in enumerate(self.mid_ranks) :
            deviation = mRank - self.end_ranks[idx]

            if deviation > 0 : 
                deviation = '↑' + str(abs(deviation))

            elif deviation < 0 :
                deviation = '↓' + str(abs(deviation))
            
            else :
                deviation = '=' + str(abs(deviation))

            print(f'mid_rank : {mRank} \t end_rank : {self.end_ranks[idx]} \t deviation : {deviation}')
    
