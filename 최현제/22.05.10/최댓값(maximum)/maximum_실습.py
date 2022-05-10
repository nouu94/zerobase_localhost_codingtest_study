# 리스트에서 아스키코드가 가장 큰 값을 찾는 알고리즘을 만들어보자.
# 아스키 코드끼리 비교하여 가장 값이 큰 아스키 코드를 출력하는 클래스
class MaxAlgorithm : 

    def __init__(self, cs) :
        self.chars = cs 
        self.maxChar = 0

    
    def getMaxChar(self) : 

        self.maxChar = self.chars[0]

        for c in self.chars :
            if ord(self.maxChar) < ord(c) :
                self.maxChar = c


        return self.maxChar

# 만든 클래스를 이용해 출력
chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']
mc = MaxAlgorithm(chars)
maxChar = mc.getMaxChar()

print(f'maxChar : {maxChar}')