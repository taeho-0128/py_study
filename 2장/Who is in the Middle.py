#그릇 1
bowl1 = int(input())

#그릇 2
bowl2 = int(input())

#그릇 3
bowl3 = int(input())

#중간 그릇이 엄마곰의 것(mom_bowl)

#그릇 1이 중간인 경우 3 1 2 or 2 1 3
if ((bowl1 <= bowl2 and bowl1 >=  bowl3) or (bowl1 <= bowl3 and bowl1 >= bowl2)):
    mom_bowl = bowl1

#그릇 2가 중간인 경우 1 2 3 or 3 2 1
elif ((bowl2 <= bowl1 and bowl2 >=  bowl3) or (bowl2 <= bowl3 and bowl2 >= bowl1)):
    mom_bowl = bowl2

#나머지 (그릇 3이 중간인 경우  2 3 1 or  1 3 2
else:
    mom_bowl = bowl3

print(mom_bowl)