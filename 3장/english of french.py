
line_cnt = int(input())

t_cnt = 0
s_cnt = 0

if not 0 < line_cnt <10000:
    exit('라인 수 초과')

#t와 s의 수를 구함
for i in range(line_cnt):
    line = input()
    for char in line:
        if char == 'T':
            t_cnt += 1
        if char == 't':
            t_cnt += 1
        if char == 'S':
            s_cnt += 1
        if char == 's':
            s_cnt += 1


#t가 많으면 영어
if t_cnt > s_cnt:
    print('English')
#s가 많으면 프랑스어
elif t_cnt < s_cnt:
    print('French')
#둘이 같아도 프랑스어
else: # t_cnt = s_cnt:
    print('French')