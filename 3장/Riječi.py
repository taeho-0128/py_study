pressed = input()
if not pressed.isdigit():
    exit("문자열이 숫자로만 이루어져있지 않음")
pressed = int(input())
if not 1 <= pressed <= 45:
    exit("범위를 벗어남")

cnt_a = 1
cnt_b = 0

for i in range(pressed):
    next_cnt_a = cnt_b
    next_cnt_b = cnt_a + cnt_b
    cnt_a = next_cnt_a
    cnt_b = next_cnt_b

print(cnt_a,cnt_b)