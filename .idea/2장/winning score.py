apple3 = int(input())
apple2 = int(input())
apple1 = int(input())
banana3 = int(input())
banana2 = int(input())
banana1 = int(input())

appletotal = apple3*3 + apple2*2 + apple1
bananatotal = banana3*3 + banana2*2 + banana1

if appletotal > bananatotal:
    print('A')
elif bananatotal > appletotal:
    print('B')
else:
    print('T')