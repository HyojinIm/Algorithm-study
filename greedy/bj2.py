import sys

n = int(sys.stdin.readline().rstrip())
meetings = []
answer = 0
for i in range(n):
    meetings.append(list(map(int, sys.stdin.readline().rstrip().split())))

# meetings.sort(key=lambda x:x[0])

# for i, v in enumerate(meetings):
#     if answer >= len(meetings)-i+1:
#         break
#     finish = v[1]
#     temp = 1
#     for j in range(i+1, len(meetings)):
#         if meetings[j][0]>=finish:
#             temp += 1
#             finish = meetings[j][1]
#     if answer < temp:
#         answer = temp


meetings.sort(key=lambda x: (x[1], x[0]))
finish = 0
for i in meetings:
    if i[0] >= finish:
        answer += 1
        finish = i[1]

print(answer)