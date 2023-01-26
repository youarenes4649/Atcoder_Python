

N,Q = map(int,input().split())
A = [i for i in range(1,N+1)]
flip = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x,y = q[1:]
        A[x-1] = y
    elif q[0] == 2: 
        flip = 1 - flip
    else:
        x = q[1]
        if flip:
            print(A[::-1][x-1])
        else:
            print(A[x-1])
        
            
