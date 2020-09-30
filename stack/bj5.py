import sys

a = []
answer = []
count = 1
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    while count <= temp:
        a.append(count)
        count += 1
        answer.append("+")
    if temp == a[len(a)-1]:
        a.pop()
        answer.append("-")
    else:
        answer.clear()
        answer.append("NO")
        break

for i in answer:
    print(i)