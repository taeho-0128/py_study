

songs = 'ABCDE'

button = 0

while button != 4:
    button = int(input())
    if not 1<= button <=4:
        exit('번호가 1~4회가 아닙니다.')
    pressCount = int(input())
    if not 1 <= pressCount <= 10:
        exit("버튼 누르는 횟수가 1~10회가 아닙니다.")

    while pressCount > 0:
        pressCount -= 1
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]

output = ''
for song in songs:
    output = output + song +' '
print(output[:-1])