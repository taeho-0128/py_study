# When You Eat Your Smarties
# ecoo15r1p1

MAX_GRIP = 7
RED_EAT_TIME = 16
GRIP_EAT_TIME = 13

testcase = 1
results = []

for i in range(testcase):
    limit = 200
    time = 0
    red = 0
    count = 0

    while limit > 0:
        smaties = input()
        limit -= 1

        count += 1
        if smaties == 'red':
            red += 1

        if count == MAX_GRIP:
            if red == count:
                time += red * RED_EAT_TIME
            else:
                time += red * RED_EAT_TIME
                time += GRIP_EAT_TIME
            red = 0
            count = 0


        if smaties == "end of box":
            if count > 0:
                if red == count:
                    time += red * RED_EAT_TIME
                else:
                    time += red * RED_EAT_TIME
                    time += GRIP_EAT_TIME
            break

    results.append(time)

for result in results:
    print(result)