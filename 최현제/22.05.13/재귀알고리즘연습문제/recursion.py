# 다음은 'A상사'의 21년 월별 매출을 나타내는 표이다. 재귀알고리즘을 사용해서 
# 1월부터 12월까지 전월대비 매출 증감액을 나타내는 프로그램을 만들어보자.

def salesUpAndDown(ss) : 

    if len(ss) == 1 : 
        return ss

    print(f'sales : {ss}')

    current_sales = ss.pop(0) # 1200, [1300, 12500, 11000 ...]
    next_sales = ss[0] # 1300

    increase = next_sales - current_sales
    if increase > 0 : 
        increase = '+' + str(increase)
    print(f'매출 증감액 : {increase}')

    return salesUpAndDown(ss)

    

sales = [12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]
a = salesUpAndDown(sales)
print(a)