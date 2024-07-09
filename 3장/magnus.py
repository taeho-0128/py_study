letter = input()

#letter 은 1~100,000사이
if not 1 <= len(letter) <= 100000:
    exit('1~100,000이 아님')

cnt_HONI = 0
position = 0

for char in letter:
    if position == '1':
        match = 'H'



