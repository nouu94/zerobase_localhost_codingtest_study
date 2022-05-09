import random 
import sortMod as sm

nums = random.sample(range(1, 1000), 100)
print(f'not sorted numbers : {nums}')

# 객체 생성 
sn = sm.SortNumbers(nums)

# 오름차순 asc
sn.setSort()
sortedNumbers = sn.getSortedNumbers()
print(f'sortedNumbers by ASC : {sortedNumbers}')

print()

# 내림차순 desc
sn.isAscending(False) 
sn.setSort()
sortedNumbers = sn.getSortedNumbers()
print(f'sortedNumbers by DESC : {sortedNumbers}')

# min & max 
print(f'min : {sn.getMinimumNumber()}')
print(f'max : {sn.getMaxNumber()}')


