# 1부터 1000까지의 난수 100개를 생성하고, 다음의 요구 사항을 만족하는 모듈을 만들어보자. 

# 생선된 난수들을 오름 차순 또는 내림 차순으로 정렬하는 알고리즘 구현 
# 생성된 난수 중 최솟값, 최댓값을 반환하는 함수 구현 

class SortNumbers : 

    # ns, ascending = True
    def __init__(self, ns, asc = True) : 
        self.nums = ns
        self.isAsc = asc


    def isAscending(self, flag) : 
        self.isAsc = flag


    def setSort(self) : 

        for i1 in range(1, len(self.nums)) :
            i2 = i1 - 1
            current_num = self.nums[i1]

            if self.isAsc : 
                while self.nums[i2] > current_num and i2 >= 0 :
                    self.nums[i2 + 1] = self.nums[i2]
                    i2 -= 1

            else :
                while self.nums[i2] < current_num and i2 >= 0 :
                    self.nums[i2 + 1] = self.nums[i2]
                    i2 -= 1

            self.nums[i2 + 1] = current_num


    def getSortedNumbers(self) : 
        return self.nums



    def getMinimumNumber(self) :
        if self.isAsc :
            return self.nums[0]
        else :
            return self.nums[-1]


    def getMaxNumber(self) :
        if self.isAsc :
            return self.nums[-1]
        else :
            return self.nums[0]