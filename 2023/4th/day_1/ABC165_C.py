import sys
sys.setrecursionlimit(10 ** 7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 

N,M,Q = mi()
query = []
for i in range(Q):
    a,b,c,d = mi()
    #0idxに合わせる
    query.append((a - 1,b - 1,c,d))
    
ans = 0
def dfs(A):
    global ans
    if len(A) == N:
        total = 0
        for q in query:
            a,b,c,d = q
            if A[b] - A[a] == c:
                total += d
        return total
    
    for i in range(A[-1],M+1):
        ans = max(ans,dfs(A + [i]))
        
    return ans

print(dfs([1]))