
PRIZE1 = 30
PRIZE_COUNT1 = 35
PRIZE2 = 60
PRIZE_COUNT2 = 100
PRIZE3 = 9
PRIZE_COUNT3 = 10

coin = input()
if not coin.isdigit():exit(f"{coin} is not number")
coin = int(coin)
if not 3 <= coin <= 1000:exit(f"coin out range(3 <= {coin} <= 1000)")

machine1State = input()
if not machine1State.isdigit():exit(f"{machine1State} is not number")
machine1State = int(machine1State)
if not 0 <= machine1State <= PRIZE_COUNT1:
    exit(f"machine1State out range(0 <= {machine1State} <= {PRIZE_COUNT1})")

machine2State = input()
if not machine2State.isdigit():exit(f"{machine2State} is not number")
machine2State = int(machine2State)
if not 0 <= machine2State <= PRIZE_COUNT2:
    exit(f"machine1State out range(0 <= {machine2State} <= {PRIZE_COUNT2})")


machine3State = input()
if not machine3State.isdigit():exit(f"{machine3State} is not number")
machine3State = int(machine3State)
if not 0 <= machine3State <= PRIZE_COUNT3:
    exit(f"machine1State out range(0 <= {machine3State} <= {PRIZE_COUNT3})")


isBroken = False
limit = 10000
seat = playCount = 0
while limit > 0 and not isBroken:
    limit -= 1
    base = coin + seat #왜 base를 쓰지?? base가 뭐지??
    a = int(base / 3)
    b = base % 3
    #코인을 기게수로 나눈 후 몫 만큼 각 기계의 사용량에 반영됨
    machine1State += a
    machine2State += a
    machine3State += a

    #나머지 만큼 기계 1,2,3 번에 추가 되어야 하는데 나머지에 따라 몇번 기계에 추가해야하는지 달라짐
    if b == 1:
        if seat == 0: machine1State += 1
        elif seat == 1: machine2State += 1
        else: machine3State += 1
    elif b == 2:
        if seat == 0:
            machine1State += 1
            machine2State += 1
        elif seat == 1:
            machine2State += 1
            machine3State += 1
        else:
            machine3State += 1
            machine1State += 1
playCount += coin
seat = (seat + coin) % 3
coin = 0

if machine1State >= PRIZE_COUNT1:
    coin += int(machine1State / PRIZE_COUNT1) * PRIZE1
    machine1State = machine1State % PRIZE_COUNT1
if machine2State >= PRIZE_COUNT2:
    coin += int(machine2State / PRIZE_COUNT2) * PRIZE2
    machine2State = machine2State % PRIZE_COUNT2
if machine3State >= PRIZE_COUNT3:
    coin += int(machine3State / PRIZE_COUNT3) * PRIZE3
    machine3State = machine3State % PRIZE3

if coin == 0: isBroken = True
