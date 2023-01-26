from itertools import accumulate
import bisect
N,Q=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
sum_A=list(accumulate(A))
for q in range(Q):
    x=int(input())
    loc=bisect.bisect_right(A,x)
    if loc==N:
        print(x*loc-sum_A[N-1])
        continue

    if loc==0:
        print(sum_A[N-1]-N*x)
        continue
    else:

        ans=x*loc-sum_A[loc-1]
        
        ans+=sum_A[N-1]-sum_A[loc-1]
        ans-=x*(N-loc)
        print(ans)
