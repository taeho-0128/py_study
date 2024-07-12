PARKED = 'C'
EMPTY = '.'

spaces = input()
if not spaces.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")

spaces = int(spaces)
if not 1 <= spaces <= 100:
    exit("범위를 벗어남(1 <= n <= 100)")

yesterday = input()
if yesterday.count(PARKED) + yesterday.count(EMPTY) != spaces:
    exit("잘못된 입력값('C', '.'만 입력 가능, space만큼 입력 필요)")

today = input()
if today.count(PARKED) + today.count(EMPTY) != spaces:
    exit("잘못된 입력값('C', '.'만 입력 가능, space만큼 입력 필요)")

continuousParking = 0
for i in range(spaces):
    if yesterday[i] == PARKED and today[i] == yesterday[i]:
        continuousParking += 1
print(continuousParking)