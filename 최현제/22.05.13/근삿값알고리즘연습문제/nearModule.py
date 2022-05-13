class NearAlgorithm :

    def __init__(self, d) : 
        self.temps = {0: 24, 5: 22, 10: 20, 15: 16, 20: 13, 25: 10, 30: 6}
        self.depth = d
        self.near_num = 0
        self.min_num = 24


    def getNearNumbers(self) :

        for n in self.temps.keys() : 
            abs_num = abs(n - self.depth)

            if abs_num < self.min_num :
                self.min_num = abs_num
                self.near_num = n

        return self.temps[self.near_num]
        

        