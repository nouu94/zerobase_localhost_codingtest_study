# 자료구조에서 가장 큰 값을 찾는다. 
# nums = [-2, -4, 5, 7, 10, 0, 8, 20, -11]
# max_num = nums[0]
# max_num < nums[1], nums[2], nums[3].... nums[n]

class MaxMinAlgorithm :

    def __init__(self, nums) : 
        self.nums = nums
        self.max_num = 0
        self.min_num = self.nums[0]


    def getMaxNum(self) : 
        self.max_num = self.nums[0]


        for n in self.nums :
            if self.max_num < n :
                self.max_num = n

        return self.max_num


    # def getMinNum(self) : 

    #     self.min_num = self.nums[0]

    #     for n in self.nums :
    #         if self.min_num > n :
    #             self.min_num = n

    #     return self.min_num



ma = MaxMinAlgorithm([-2, -4, 5, 7, 10, 0, 8, 20, -11])
max_num = ma.getMaxNum()
# min_num = ma.getMinNum()

print(f'max_num : {max_num}')
# print(f'min_num : {min_num}')