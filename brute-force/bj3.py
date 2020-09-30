import sys
n = int(sys.stdin.readline().rstrip())
people = []
for i in range(n):
    person = sys.stdin.readline().rstrip()
    people.append([int(i) for i in person.split()])

answer = [n+1]*n
a = [i[0] for i in people]
b = [i[1] for i in people]
for i in range(1,n+1):
    flag = False
    for j, v in enumerate(people):
        if v[0] == max(a) and v[1] == max(b):
            answer[j] = i
            flag = True
            a.remove(v[0])
            b.remove(v[1])
    if not flag:
        for j, v in enumerate(people):
            if answer[j] >= i:
                if v[0] < max(a) and v[1] < max(b):
                    answer[j] = i + 1
                else:
                    answer[j] = i

            
print(answer)