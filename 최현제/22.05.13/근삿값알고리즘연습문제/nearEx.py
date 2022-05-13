# 근삿값 알고리즘 
# 다음 표는 수심에 따른 수온을 나타내고 있다. 근사값 알고리즘을 이용해서 
# 수심을 입력하면 수온을 출력하는 모듈을 만들어보자.

import nearModule 

depth = int(float(input('input depth : ')))
print(f'depth : {depth}m')

na = nearModule.NearAlgorithm(depth)
temp = na.getNearNumbers()

print(f'water temperature : {temp}')


