class MaxAlgorithm : 

    def __init__(self, ns) : 
        self.nums = ns
        self.max_num = 0
        self.max_num_idx = 0


    def setMaxNumIdxAndNum(self) :
        self.max_num = self.nums[0]
        self.max_num_idx = 0

        for i, n in enumerate(self.nums) : 
            if self.max_num < n :
                self.max_num = n
                self.max_num_idx = i


    def getMaxNum(self) : 
        return self.max_num

    def getMaxNumIdx(self) : 
        return self.max_num_idx