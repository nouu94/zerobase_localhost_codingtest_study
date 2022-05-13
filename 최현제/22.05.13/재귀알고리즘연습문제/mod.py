class NumsSum : 

    def __init__(self, n1, n2) :

        self.big_num = 0
        self.small_num = 0
        self.setN1N2(n1, n2)

    

    def setN1N2(self, n1, n2) : 
        self.big_num = n1
        self.small_num = n2

        if n1 < n2 : 
            self.big_num = n2
            self.small_num = n1

    
    def addNum(self, n) : 
        if n <= 1 :
            return n

        return n + self.addNum(n - 1)

    
    def sumBetweenNums(self) : 
        return self.addNum(self.big_num - 1) - self.addNum(self.small_num - 1)

        

        