#Munch 'n' Brunch
#ecoo17r1p1


YEAR_COST = [12, 10, 7, 5]

for dataset in range(10):
    trip_cost = input()
    if not trip_cost.isdigit():
        exit('수학여행 비용이 숫자가 아님')
    trip_cost = int(trip_cost)

    propotions = input().split()

    student_num = input()
    if not student_num.isdigit():
        exit('학생 수가 숫자가 아님')
    student_num = int(student_num)


    for i in range(len(propotions)):
        propotions[i] = float(propotions[i])

    student_per_year = []

    for propotion in propotions:
        students = int(student_num * propotion)
        student_per_year.append(students)
        counted_student = sum(student_per_year)
        uncounted_student = student_num - counted_student
        mostyear = max(student_per_year)
        where = student_per_year.index(mostyear)
        student_per_year[where] = student_per_year[where] + uncounted_student

        total_raised = 0

    for i in range(len(student_per_year)):
        total_raised = total_raised + student_per_year[i] * YEAR_COST[i]

    if total_raised / 2 < trip_cost:
        print('YES')
    else:
        print('NO')
