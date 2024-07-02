month = int(input())
day = int(input())

if month <= 0 or month > 12:
    exit()
if day <= 0 or day > 31:
    exit()

# 1월
if month > 2:
    print("After")

#3월부터 12월까지
elif month < 2:
    print("Before")

#2월인 경우
else:
    if day < 18:
        print("Before")
    elif day > 18:
        print("After")
    else:
        print("Special")