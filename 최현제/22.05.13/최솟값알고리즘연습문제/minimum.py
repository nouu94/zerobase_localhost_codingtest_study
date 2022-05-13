class MinAlgorithm : 

    def __init__(self, ns) : 

        self.nums = ns
        self.min_num = 0
        self.min_num_cnt = 0

    def setMinNum(self) : 
        self.min_num = 51

        for n in self.nums :
            if self.min_num > n : 
                self.min_num = n


    def getMinNum(self) : 
        self.setMinNum()

        return self.min_num


    def setMinNumCnt(self) : 
        self.setMinNum()

        for n in self.nums : 
            if self.min_num == n : 
                 self.min_num_cnt += 1
            

    def getMinNumCnt(self) : 
        self.setMinNumCnt()

        return self.min_num_cnt
    