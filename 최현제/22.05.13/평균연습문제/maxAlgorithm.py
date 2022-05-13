class MaxAlgorithm : 

    def __init__(self, ss) : 
        self.scores = ss
        self.max_score = 0
        self.max_idx = 0

    
    def removeMaxScore(self) : 
        self.max_score = self.scores[0]

        for i, s in enumerate(self.scores) : 
            if self.max_score < s : 
                self.max_score = s
                self.max_idx = i

        print(f'self.max_score : {self.max_score}')
        print(f'self.max_idx : {self.max_idx}')

        self.scores.pop(self.max_idx)
        print(f'scores : {self.scores}')