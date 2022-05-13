# 최빈값 클래스 구현 파일 

class LottoMod :

    def __init__(self, lottonumber) : 
        self.lotto_nums = lottonumber
        self.mod_list = [0 for n in range(1, 47)] # 인덱스를 구현하는 것이므로 1, 47

    
    def getLottoNumMod(self) : 
            # 회차 번호를 각각 하나씩 순회
        for round_nums in self.lotto_nums : 
            for num in round_nums : 
                self.mod_list[num] = self.mod_list[num] + 1 # 만약 num이 35라면 mod_list 인덱스 35에 1추가
        
        return self.mod_list

    def printModList(self) : 
        if sum(self.mod_list) == 0 : 
            return None

        for i, m in enumerate(self.mod_list) : 
            star = '*'
            if i != 0 :
                print(f'번호 : {i:>2}, 빈도 : {m} {star * m}')


