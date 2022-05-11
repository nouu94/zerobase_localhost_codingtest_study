class top5Players : 

    def __init__(self, cs, ns) : 
        self.currentScores = cs
        self.newScore = ns

    def setAlignScore(self) : 

        near_idx = 0
        near_score = 0
        min_num = 10.0

        for i, s in enumerate(self.currentScores) : 
            abs_num = abs(self.newScore - s)

            if abs_num < min_num : 
                min_num = abs_num
                near_idx = i
                near_score = s


        if self.newScore >= self.currentScores[i] : 
            for i in range(len(self.currentScores) - 1, near_idx, -1) : 
                self.currentScores[i] = self.currentScores[i - 1]

            self.currentScores[near_idx] = self.newScore

        else : 
            for i in range(len(self.currentScores) - 1, near_idx + 1, -1) : 
                self.currentScores[i] = self.currentScores[i - 1]

            self.currentScores[near_idx] = self.newScore

    def getFinalTop5Scores(self) : 
        return self.currentScores