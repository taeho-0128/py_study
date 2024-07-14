#ccc00s1

chips = input()

if not chips.isdigit():
    exit("칩 수량이 숫자가 아닙니다")
chips = int(chips)
if not 1 <= chips < 1000:
    exit("칩 수량이 1에서 999 사이가 아닙니다")

firstMachineUsed = input()
if not firstMachineUsed.isdigit():
    exit('첫 번째 기계 사용량이 숫자가 아닙니다')
firstMachineUsed = int(firstMachineUsed)

secondMachineUsed = input()
if not secondMachineUsed.isdigit():
    exit('두 번째 기계 사용량이 숫자가 아닙니다')
secondMachineUsed = int(secondMachineUsed)

thirdMachineUsed = input()
if not thirdMachineUsed.isdigit():
    exit('세 번째 기계 사용량이 숫자가 아닙니다')
thirdMachineUsed = int(thirdMachineUsed)

plays = 0
machinenum = 1

while chips >= 1:
    chips -= 1

    if machinenum == 1:
        firstMachineUsed += 1
        if firstMachineUsed % 35 == 0:
            chips += 30

    elif machinenum == 2:
        secondMachineUsed += 1
        if secondMachineUsed % 100 == 0:
            chips += 60

    elif machinenum == 3:
        thirdMachineUsed += 1
        if thirdMachineUsed % 10 == 0:
            chips += 9

    plays += 1
    machinenum += 1
    if machinenum == 4:
        machinenum = 1

print('Martha plays', plays, 'times before going broke.')