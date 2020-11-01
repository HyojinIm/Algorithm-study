import sys

def star(n):
    if n == 1:
        return '*'
    else:
        temp = star(n//3)
        result = ['' for i in range(n)]
        for i in range(n):
            if i>=n/3 and i<2*n/3:
                result[i] += temp[i%(n//3)]+' '*len(temp[i%(n//3)])+temp[i%(n//3)]
            else:
                result[i] += temp[i%(n//3)]*3
        return result

N = int(sys.stdin.readline().rstrip())
for i in star(N):
    print(i)