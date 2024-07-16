# When You Eat Your Smarties
# ecoo15r1p1

MAX_GRIP = 7
RED_EAT_TIME = 16
GRIP_EAT_TIME = 13

testcase = 10
results = []

for i in range(testcase):
    limit = 200
    time = 0
    red = 0
    count = 0

    while limit > 0:
        smarties = input()
        limit -= 1

        if smarties == "end of box":
            if count > 0:
                if red == count:
                    time += red * RED_EAT_TIME
                else:
                    time += GRIP_EAT_TIME
                    time += red * RED_EAT_TIME
            break
        count += 1

        if smarties == "red":
            red += 1

        if count == MAX_GRIP:
            if red == MAX_GRIP:
                time += red * RED_EAT_TIME
            else:
                time += GRIP_EAT_TIME
                time += red * RED_EAT_TIME
            red = 0
            count = 0


    if count > 0:
        if red == count:
            time += red * RED_EAT_TIME
        else:
            time += GRIP_EAT_TIME
            time += red * RED_EAT_TIME

    results.append(time)

for result in results:
    print(result)