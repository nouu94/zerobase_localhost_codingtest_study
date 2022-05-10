# 최솟값 : 가장 작은 값을 찾자!
# nums = [-2, -4, 5, 7, 10, 0 ,8, 20, -11]
# min_num = nums[0]
# min_num > nums[1], nums[2], nums[3].... nums[n]

class MinAlgorithm : 

    def __init__(self, ns) : 
        self.nums = ns 
        self.min_num = self.nums[0]

    def getMinNum(self) : 

        for n in self.nums : 
            if self.min_num > n : 
                self.min_num = n

        return self.min_num


ma = MinAlgorithm([-2, -4, 5, 7, 10, 0, 8, 20, -11])
min_num = ma.getMinNum()
print(f'min_num : {min_num}')


