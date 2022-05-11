# 재귀 알고리즘을 이용해서 최대 공약수를 계산하는 알고리즘 
# 유클리드 호제법 
# 두 자연수 n1, n2에 대하여 (n1 > n2) n1를 n2로 나눈 나머지를 r이라고 할 때 
# n1과 n2의 최대공약수는 n2와 r의 최대공약수와 같다. 

def uclid(n1, n2) : 
    if n1 % n2 == 0 : 
        return n2
    else :
        return uclid(n2, n1 % n2)

# def gcd2(n1, n2) : 
#     max_num = 0
#     for i in range(1, (n1 + 1)) : 
#         if n1 % i == 0 and n2 % i == 0 :
#             max_num = i
    
#     return max_num

print(f'uclid(82, 32) : {uclid(82, 32)}')
print(f'uclid(96, 40) : {uclid(96, 40)}')

