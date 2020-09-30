from itertools import combinations
import sys

a = sys.stdin.readline().rstrip()
items = sys.stdin.readline().rstrip()

a = [int(i) for i in a.split()]
items = list(map(int, items.split()))

lst = list(combinations(items,3))
# min = a[1]
# for i in lst:
#     if sum(i) <= a[1]:
#         if a[1] - sum(i) < min:
#             min = a[1] - sum(i)
#             answer = sum(i)
temp = []
for i in lst:
    if sum(i) <= a[1]:
        temp.append(sum(i))
print(max(temp))