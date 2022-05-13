# 최솟값 알고리즘을 이용해서 숫자로 이루어진 리스트에서 최솟값과 최솟값의 
# 개수를 찾는 모듈을 만들어보자 
# (리스트는 1부터 50까지의 난수 30개를 이용하되, 중복이 허용되도록 한다.)

import random
import minimum

if __name__ == "__main__":
    nums = []

    for _ in range(30) :
        nums.append(random.randint(1, 50)) 

    print(f'nums : {nums}')

    ma = minimum.MinAlgorithm(nums)
    print(f'min : {ma.getMinNum()}')
    print(f'min num cnt: {ma.getMinNumCnt()}')




    


