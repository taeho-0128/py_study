mbPerMonth = input()
if not mbPerMonth.isdigit():
    exit(f"{mbPerMonth}이 숫자로만 이루어져 있지 않음")
mbPerMonth = int(mbPerMonth)
if not 1 <= mbPerMonth <= 1000:
    exit(f"범위를 벗어남(1 <= {mbPerMonth} <= 1000)")

spendMonths = input()
if not spendMonths.isdigit():
    exit(f"{spendMonths}이 숫자로만 이루어져 있지 않음")

spendMonths = int(spendMonths)
if not 1 <= spendMonths <= 100:
    exit(f"범위를 벗어남(1 <= {spendMonths} <= 100)")

availableMb = mbPerMonth * (spendMonths + 1)

for i in range(spendMonths):
    spendMb = input()
    if not spendMb.isdigit():
        exit(f"{spendMb}이 숫자로만 이루어져 있지 않음")

    spendMb = int(spendMb)
    if not 1 <= spendMb <= 10000:
        exit(f"범위를 벗어남(1 <= {spendMb} <= 10000)")

    availableMb -= spendMb
    if availableMb < 0:
        exit("사용한 데이터가 가용한 데이터를 초과합니다")

print(availableMb)
