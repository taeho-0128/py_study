
K = int(input())

cnt_a = 1
cnt_b = 0

for i in range(K):
    next_cnt_a = cnt_b
    next_cnt_b = cnt_a + cnt_b
    cnt_a = next_cnt_a
    cnt_b = next_cnt_b

print(cnt_a,cnt_b)