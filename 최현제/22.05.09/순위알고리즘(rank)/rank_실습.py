# 순위 실습 순위를 정하자 
# 학급 학생(20명) 들의 중간고사와 기말고사 성적을 이용해서 각각의 순위를 구하고, 중간고사 대비 기말고사 순위 변화(편차)를 출력하는 프로그램을 만들어 보자. (시험 성적은 난수를 이용한다.)

# 클래스 없이 한 파일 내에 문제 풀이 
# import random 

# mid_stu_scos = random.sample(range(50, 101), 20)
# mid_rank = [0 for _ in range(len(mid_stu_scos))]

# end_stu_scos = random.sample(range(50, 101), 20)
# end_rank = [0 for _ in range(len(end_stu_scos))]

# for standard_idx, standard_score in enumerate(mid_stu_scos) : 

#     for loop_score in mid_stu_scos : 
        
#         if standard_score < loop_score : 
#             mid_rank[standard_idx] += 1


# for standard_idx, standard_score in enumerate(end_stu_scos) : 

#     for loop_score in end_stu_scos :

#         if standard_score < loop_score : 
#             end_rank[standard_idx] += 1

# print(f'mid_stu_scos : {mid_stu_scos}')
# print(f'mid_rank : {mid_rank}')

# print(f'end_stu_scos : {end_stu_scos}')
# print(f'end_rank : {end_rank}')

# for idx in range(len(mid_stu_scos)) : 

#     if mid_rank[idx] - end_rank[idx] > 0 :
#         print(f'mid_rank: {mid_rank[idx] + 1}\t end_rank: {end_rank[idx] + 1}\t Deviation: ↑{mid_rank[idx] - end_rank[idx]}')

#     elif mid_rank[idx] - end_rank[idx] < 0 :
#         print(f'mid_rank: {mid_rank[idx] + 1}\t end_rank: {end_rank[idx] + 1}\t Deviation: ↓{end_rank[idx]- mid_rank[idx]}')

#     elif mid_rank[idx] - end_rank[idx] == 0 :
#         print(f'mid_rank: {mid_rank[idx]}\t end_rank: {end_rank[idx]}\t Deviation: ={mid_rank[idx] - end_rank[idx]}')

# 클래스 있을 시 구현 프로그래밍이 조금 길어지니 모듈을 만들어 해결 
# rankMode와 rankEx 파일에 있음

