# 사용자가 정수 두개를 입력하면 작은 정수와 큰 정수 사이의 모든 정수의 합을 구하는 
# 프로그램을 재귀 알고리즘을 이용해서 만들어보자. 

import mod 

num1 = int(input(f'input number1 : '))
num2 = int(input(f'input number2 : '))

ns = mod.NumsSum(num1, num2)
result = ns.sumBetweenNums()
print(f'result : {result}')

