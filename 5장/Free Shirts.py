#Free Shirts
#ecoo19r1p1

for i in range(10):
    data = input()
    datalist = data.split()
    print(datalist)

    cleanshirt = datalist[0]
    eventcnt = datalist[1]
    totalday = datalist[2]

    if not cleanshirt.isdigit():
        exit('셔츠 수가 숫자가 아님')
    cleanshirt = int(cleanshirt)
    if not 1 <= cleanshirt <= 100:
        exit('셔츠 수가 1~100이 아님')

    if not eventcnt.isdigit():
        exit('이벤트 수가 숫자가 아님')
    eventcnt = int(eventcnt)
    if not 1 <= eventcnt <= 100:
        exit('이벤트 수가 1~100이 아님')

    if not totalday.isdigit():
        exit('전체 날 수가 숫자가 아님')
    totalday = int(totalday)
    if not 1 <= totalday <= 1000:
        exit('전체 날 수가 1~1000이 아님')

    laundry = 0
    eventday = input().split()
    totalshirt = cleanshirt
    for day in range(totalday):
        cleanshirt -= 1
        if cleanshirt == 0:
            laundry += 1
            cleanshirt = totalshirt

        if day in eventday:
            cleanshirt += 1
    print(laundry)



