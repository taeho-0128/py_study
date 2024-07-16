tomorrow_startnum = int(input())

limit = 1000000
TAKE_count = 0
SERVE_count = 0

while limit > 0:
    limit -= 1
    status = input()

    if status == 'TAKE':
        TAKE_count += 1
        tomorrow_startnum += 1
        if tomorrow_startnum > 999:
            tomorrow_startnum = 1
    elif status == 'SERVE':
        SERVE_count += 1
    elif status == "CLOSE":
        waiting_students = TAKE_count - SERVE_count
        print(f"{TAKE_count} {waiting_students} {tomorrow_startnum}")
        TAKE_count = 0
        SERVE_count = 0
    elif status == "EOF":
        break