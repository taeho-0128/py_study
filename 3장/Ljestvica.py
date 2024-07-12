sequence = input()

cnt_A_minor = 0
cnt_C_major = 0

# 첫 번째 값이거나 마디 구분 다음에 오는 값이 A단조 주음인지 C장조 주음인지 파악해 카운트
for i in range(len(sequence)):
    if i == 0 or sequence[i-1] == '|':
        if sequence[i] in ['A', 'D', 'E']:
            cnt_A_minor += 1
        elif sequence[i] in ['C', 'F', 'G']:
            cnt_C_major += 1

# 수가 같은 경우 마지막 코드가 A이면 A단조 아니면 C장조
if cnt_A_minor == cnt_C_major:
    if sequence[-1] == 'A':
        cnt_A_minor += 1
    elif sequence[-1] == 'C':
        cnt_C_major += 1

if cnt_A_minor > cnt_C_major:
    print('A-mol')
else:
    print('C-dur')