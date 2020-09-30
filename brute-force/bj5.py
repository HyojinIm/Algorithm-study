import sys
n = int(sys.stdin.readline().rstrip())
count = 1
i = 0
while True:
    i += 1
    if '666' in str(i):
        if count == n:
            print(i)
            break
        count +=1