N, X, Y = map(int, input().split())
A = [int(x) for x in input().split()]
DX, DY = [], []
for i in range(1, N):
    if i%2:
        DY.append(A[i])
    else:
        DX.append(A[i])
dpX = set([A[0]])
for dx in DX:
    nxt = []
    for x in dpX:
        if x+dx <= X+1000:
            nxt.append(x+dx)
        if x-dx >= X-1000:
            nxt.append(x-dx)
    dpX = set(nxt)

dpY = set([0])
for dy in DY:
    nxt = []
    for y in dpY:
        if y+dy <= Y+1000:
            nxt.append(y+dy)
        if y-dy >= Y-1000:
            nxt.append(y-dy)
    dpY = set(nxt)

if X in dpX and Y in dpY:
    print('Yes')
else:
    print('No')
