import sys

formula = sys.stdin.readline().rstrip()
minus = formula.split('-')
result = sum(list(map(int, minus.pop(0).split('+'))))
for i in minus:
    plus = list(map(int, i.split('+')))
    result -= sum(plus)
print(result)