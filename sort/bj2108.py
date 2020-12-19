import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for i in range(N)]

print(round(sum(nums)/N))

nums.sort()
print(nums[N//2])

# counts = [nums.count(i) for i in nums]
# maxCount = max(counts)
# most = [nums[i] for i in range(N) if counts[i]==maxCount]
# most = list(set(most))
# if len(most)>=2:
#     print(nums[most[1]])
# else:
#     print(nums[most[0]])
cnt = Counter(nums)
cnt_tuple = cnt.most_common()
max_cnt = cnt_tuple[0][1]
most = []
for i in cnt_tuple:
    if i[1] == max_cnt:
        most.append(i[0])
if len(most)>1:
    most.sort()
    print(most[1])
else:
    print(most[0])

print(max(nums)-min(nums))