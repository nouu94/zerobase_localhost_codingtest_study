class Top5Players : 
    # cts : current scores
    def __init__(self, cts, ns) : 
        self.current_scores = cts
        self.new_score = ns


    def setAlignScore(self) : 
        near_idx = 0
        min_num = 10.0

        for i, s in enumerate(self.current_scores) : 
            abs_num = abs(self.new_score - s)
            if abs_num < min_num : 
                min_num = abs_num
                near_idx = i

        if self.new_score >= self.current_scores[near_idx] :
            for i in range(len(self.current_scores) - 1, near_idx, -1) : 
                self.current_scores[i] = self.current_scores[i-1]
            self.current_scores[near_idx] = self.new_score

        else : 
            for i in range(len(self.current_scores) - 1, near_idx + 1, -1) : 
                self.current_scores[i] = self.current_scores[i-1]
            self.current_scores[near_idx + 1] = self.new_score

    
    def getFinalTop5Scores(self) : 
        return self.current_scores
            


