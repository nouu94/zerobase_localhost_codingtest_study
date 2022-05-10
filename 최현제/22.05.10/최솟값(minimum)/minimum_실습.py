# 최솟값(실습) : 가장 작은 값을 찾자! 
# 리스트에서 아스키코드가 가장 작은 값을 찾는 알고리즘을 만들어보자.

class MinAlgorithm : 

    def __init__(self, cs) : 
        self.chars = cs
        self.min_char = 0


    def getMinChar(self) : 
        self.min_char = self.chars[0]

        for c in self.chars : 
            if ord(self.min_char) > ord(c) : 
                self.min_char = c

        return self.min_char

ma = MinAlgorithm(['c', 'x', 'Q', 'a', 'e', 'P', 'p'])
min_char = ma.getMinChar()
print(f'min_char : {min_char}')