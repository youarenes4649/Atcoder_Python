N = int(input())
A = list(map(int,input().split()))
from collections import defaultdict
cnt = defaultdict(int)
for i in range(len(A)):
    cnt[i+1] = A[i]
Q = int(input())
for _ in range(Q):
    q = list(map(int,input().split()))
    
    if q[0] == 1 :
        k,x = q[1:]
        cnt[k] = x
    else:
        print(cnt[q[1]])
        
    