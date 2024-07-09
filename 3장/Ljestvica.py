# A, D, E 는 A단조 주음
# C, F, G 는 c장조 주음
# 마디 구분 다음에 오는 값이 A단조 주음이 많냐 C장조 주음이 많냐에 따라 A단조인지 C장조인지 파악


#곡의 흐름
sequence = input()

cnt_A_minor = 0
cnt_C_major = 0

#첫번째 값이거나 마디 다음에 오는 값이 A단조 주음인지 C장조 주음인지 파악해 카운트
for i in range(len(sequence)):
    if i == 0 or sequence[i-1] == '|':
        if sequence[i] == 'A':
            cnt_A_minor += 1
        if sequence[i] == 'D':
            cnt_A_minor += 1
        if sequence[i] == 'E':
            cnt_A_minor += 1
        if sequence[i] == 'C':
            cnt_C_major += 1
        if sequence[i] == 'F':
            cnt_C_major += 1
        if sequence[i] == 'G':
            cnt_C_major += 1
    #수가 같은 경우 마지막 코드가 A이면 A단조 아니면 C장조
    if cnt_A_minor == cnt_C_major:
        if sequence[-1] == "A":
            cnt_A_minor += 1
        else:
            cnt_C_major += 1



if cnt_A_minor > cnt_C_major:
    print('A-mol')
else:
    print('c-dur')

