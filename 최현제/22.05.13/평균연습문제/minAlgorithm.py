class MinAlgorithm : 

    def __init__(self, ss) : 
        self.scores = ss
        self.min_score = 0
        self.min_idx = 0

    
    def removeMinScore(self) : 
        self.min_score = self.scores[0]

        for i, s in enumerate(self.scores) : 
            if self.min_score > s : 
                self.min_score = s
                self.min_idx = i

        print(f'self.min_score : {self.min_score}')
        print(f'self.min_idx : {self.min_idx}')

        self.scores.pop(self.min_idx)
        print(f'scores : {self.scores}')