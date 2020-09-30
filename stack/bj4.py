import sys

def checkVPS(a):
    while True:
        flag = False
        if not a:
            return True

        if a[0] == ")" or a[0] == "]":
            return False

        for i in range(len(a)-1):
            if a[i] == "(" and a[i+1] == ")":
                a.pop(i+1)
                a.pop(i)
                flag = True
                break
            if a[i] == "[" and a[i+1] == "]":
                a.pop(i+1)
                a.pop(i)
                flag = True
                break

        if flag == False:
            return False

bracket = []

while True:
    a = sys.stdin.readline().rstrip()
    if a == ".":
        break
    temp = list(a)
    for i in temp:
        if i == "(" or i == ")" or i == "[" or i == "]":
            bracket.append(i)

    if(checkVPS(bracket)):
        print("yes")
    else:
        print("no")
    bracket.clear()
