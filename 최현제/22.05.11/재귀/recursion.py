# 나 자신을 다시 호출하자! 
# 나를 호출해서 함수가 계속 실행되게 하는 것
# 끝도 없이 호출될 수 있기 때문에 조건을 걸어주어야 된다.

# 반복문 대신 재귀 함수를 이용한 예 
# def recursion(num) : 

#     if num > 0 : 
#         # print('*' * num)
#         return recursion(num - 2)
#     else : 
#         return 1


# d = recursion(10)

# 10! = 10 * 9 * 8 * 7 * 6

def factorial(num) : 

    if num > 0 : 
        print(num)
        return num * factorial(num - 1)
    else : 
        return 1


factorial(5)
