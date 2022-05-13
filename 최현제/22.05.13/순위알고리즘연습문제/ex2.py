# 알파벳 문자들과 정수들에 대한 순위를 정하는 프로그램을 
# 순위 알고리즘을 이용해서 만들어보자. 단, 알파벳은 아스키코드 값을 이용한다. 
# [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']

datas = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']


ascii_datas = []
for index, data in enumerate(datas) : 

    if str(data).isalpha() : # isalpha?!
        ascii_datas.append(ord(data))
        continue

    ascii_datas.append(data)

ranks = [0 for _ in range(len(ascii_datas))]
print(f'ranks : {ranks}')

for idx, data1 in enumerate(ascii_datas):

    for data2 in ascii_datas : 
        if data1 < data2 :
            ranks[idx] += 1 # 순위 알고리즘의 핵심
        

print(f'ranks after : {ranks}')

for i, d in enumerate(datas) : 
    print(f'data : {d:>2} \t rank : {ranks[i] + 1}')



        



