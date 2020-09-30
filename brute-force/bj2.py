import sys
num = int(sys.stdin.readline().rstrip())
flag = False
for i in range(num):
    temp = 1
    sum = i
    while(temp <= i):
        sum += int(i%(temp*10)/temp)
        temp *= 10
    if sum == num:
        flag = True
        print(i)
        break
if not flag:
    print(0)