maxInfectedPeople = int(input())
firstdayInfected = int(input())
infectPerDay = int(input())

day = 0
totalInfectedPeople = firstdayInfected
currentInfected = firstdayInfected

while totalInfectedPeople <= maxInfectedPeople:
    day += 1
    newInfections = currentInfected * infectPerDay
    totalInfectedPeople += newInfections
    currentInfected = newInfections

print(day)