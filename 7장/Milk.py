input_file = open('mixmilk.in','r')
firstbucket_list = input_file.readline().split()
secondbucket_list = input_file.readline().split()
thirdbucket_list = input_file.readline().split()
input_file.close()

firstbucket_size = int(firstbucket_list[0])
firstbucket_milk = int(firstbucket_list[1])

secondbucket_size = int(secondbucket_list[0])
secondbucket_milk = int(secondbucket_list[1])

thirdbucket_size = int(thirdbucket_list[0])
thirdbucket_milk = int(thirdbucket_list[1])

def milkmix(Amilk, Bmilk, Bsize):
    if Bsize - Bmilk >= Amilk:
        return 0, Amilk + Bmilk
    else:
        return Amilk - (Bsize - Bmilk), Bsize

for i in range(100):
    if i % 3 == 0:
        firstbucket_milk, secondbucket_milk = milkmix(firstbucket_milk, secondbucket_milk, secondbucket_size)
    elif i % 3 == 1:
        secondbucket_milk, thirdbucket_milk = milkmix(secondbucket_milk, thirdbucket_milk, thirdbucket_size)
    else:
        thirdbucket_milk, firstbucket_milk = milkmix(thirdbucket_milk, firstbucket_milk, firstbucket_size)


output_file = open('mixmilk.out', 'w')
output_file.write(str(firstbucket_milk) + '\n')
output_file.write(str(secondbucket_milk) + '\n')
output_file.write(str(thirdbucket_milk) + '\n')
output_file.close()