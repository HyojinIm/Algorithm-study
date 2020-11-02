import sys

def QuadTree(N, image):
    WB = ''
    if N == 1:
        if image[0][0] == '0':
            WB += '0'
        else:
            WB += '1'
        return WB
    count = 0
    for i in image:
        count += i.count('0')
    if count!=0 and count!=N*N:
        WB += '('+QuadTree(N//2, [i[:N//2] for i in image[:N//2]])
        WB += QuadTree(N//2, [i[N//2:] for i in image[:N//2]])
        WB += QuadTree(N//2, [i[:N//2] for i in image[N//2:]])
        WB += QuadTree(N//2, [i[N//2:] for i in image[N//2:]])+')'
        return WB
    else:
        if count == 0:
            WB += '1'
        else:
            WB += '0'
        return WB

N = int(sys.stdin.readline().rstrip())
image = []
for i in range(N):
    image.append(sys.stdin.readline().rstrip())
print(QuadTree(N, image))