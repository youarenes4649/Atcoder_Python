import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
import bisect
def main():
    H,W = mi()
    S = []
    gyou = [] 
    retu = [] 
    for i in range(H):
        s = list(map(str,input()))
        S.append(s)
        
    for i in range(H):
        tmp_gyou = [0,W+1]
        for j in range(W):
            if S[i][j] == "#":
                tmp_gyou.append(j+1)
        tmp_gyou.sort()
        gyou.append(tmp_gyou)
        
    for j in range(W):
        tmp_retu = [0,H+1]
        for i in range(H):
            if S[i][j] == "#":
                tmp_retu.append(i+1)
        tmp_retu.sort()
        retu.append(tmp_retu)
  
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            h_idx = bisect.bisect_right(gyou[i],j+1)
            w_idx = bisect.bisect_right(retu[j],i+1)
            
            tmp = gyou[i][h_idx] - gyou[i][h_idx-1]
            tmp += retu[j][w_idx] - retu[j][w_idx-1] - 1
            ans = max(ans,tmp)
            
    print(ans-2)
            
            
    
        
if __name__ == '__main__':
    main()