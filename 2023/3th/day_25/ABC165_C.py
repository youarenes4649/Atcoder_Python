import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
#重複純烈の列挙
from itertools import combinations_with_replacement as cbr

def main():
    N,M,Q = mi()
    query = []
    for _ in range(Q):
        a,b,c,d = mi()
        a -= 1
        b -= 1
        query.append([a,b,c,d])
    #dfsによる全探索　単調増加という性質を使用すれば10**10ではなくなる
    
    def dfs(seq):
        ans = 0
        if len(seq) == N:
            score = 0
            for q in query:
                a,b,c,d = q
                if seq[b] - seq[a] == c:
                    score += d
                    
            return score
        
        else:
            for i in range(seq[-1],M+1):
                ne_seq = seq + [i]
                s = dfs(ne_seq)
                ans = max(ans,s)
                
        return ans
    
    ans = dfs([1])
    print(ans)
if __name__ == '__main__':
    main()