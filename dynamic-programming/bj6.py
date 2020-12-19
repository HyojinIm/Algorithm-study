import sys

N = int(sys.stdin.readline().rstrip())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

totalScore = nums[0]
for i in range(1, N):
    temp = []
    for j in range(len(nums[i])):
        if j == 0:
            temp.append(nums[i][j]+totalScore[0])
        elif j == len(nums[i])-1:
            temp.append(nums[i][j]+totalScore[-1])
        else:
            maxNum = max([totalScore[j-1], totalScore[j]])
            temp.append(nums[i][j]+maxNum)
    totalScore = temp

print(max(totalScore))