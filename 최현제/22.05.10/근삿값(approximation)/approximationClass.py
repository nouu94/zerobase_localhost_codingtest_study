def getNearNum(an) : 
    
    base_scores = [95, 85, 75, 65, 55]
    near_num = 0
    min_num = 100

    for n in base_scores :
        abs_num = abs(n - an)

        if abs_num < min_num : 
            min_num = abs_num
            near_num = n

    if near_num == 95 : 
        return 'A'
    elif near_num == 85 : 
        return 'B'
    elif near_num == 75 : 
        return 'C'
    elif near_num == 65 : 
        return 'D'
    elif near_num <= 55 : 
        return 'F'


