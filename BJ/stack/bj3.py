#a = list("(()())((()))")
#print(a)

import sys

def checkVPS(a):
    while True:
        flag = False
        if a[0] == ")":
            return "NO"
        for i in range(1, len(a)):
            if a[i] == ")":
                a.pop(i)
                a.pop(0)
                flag = True
                break

        if not a:
            return "YES"

        if flag == False:
            return "NO"

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    temp = list(sys.stdin.readline().rstrip())
    print(checkVPS(temp))
