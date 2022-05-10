# 최빈값 : 빈도수가 가장 높은 데이터를 찾자!
# 데이터에서 빈도수가 가장 많은 데이터를 최빈값이라고 한다. 

# nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]
# indexes = [0, 1, 0, 1, 0, 0, 1, 4, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1]
# len(nums) 만큼의 길이인 인덱스를 만들면 된다.
# nums의 숫자는 곧 indexes의 위치가 된다. nums의 아이템 == indexes[nums의 아이템]

# nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]

class MaxAlgorithm : 

    def __init__(self, ns) : 
        self.nums = ns
        self.max_num = 0
        self.max_num_idx = 0


    def setMaxIdxAndNum(self) : 
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


nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]

max_alo = MaxAlgorithm(nums)
max_alo.setMaxIdxAndNum()
max_num = max_alo.getMaxNum()
print(f'max_num : {max_num}')

indexes = [0 for _ in range(max_num + 1)]
print(f'indexes : {indexes}')
print(f'indexes len : {len(indexes)}')

for n in nums : 
    indexes[n] = indexes[n] + 1 

print(f'indexes : {indexes}')


maxAlo = MaxAlgorithm(indexes)
maxAlo.setMaxIdxAndNum()
max_num = maxAlo.getMaxNum()
max_num_idx = maxAlo.getMaxNumIdx()

print(f'max_num : {max_num}')
print(f'max_num : {max_num_idx}')

print(f'즉, {max_num_idx}의 빈도수가 {max_num}로 가장 높다')



