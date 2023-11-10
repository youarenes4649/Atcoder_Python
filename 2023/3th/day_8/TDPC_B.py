import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 
def main():
    tmp = li()
    A = li()
    B = li()
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    
    for l in range(len(A),-1,-1):
        for r in range(len(B),-1,-1):
            if l == len(A) and r == len(B): #どちらも全て取った時
                continue
            if (l + r) % 2 == 0: #先手がプレイ
                if l == len(A): #Aには残っていないとき
                     dp[l][r] = dp[l][r+1] + B[r] # Bのrばんめをとったから
                     
                elif r == len(B):
                    dp[l][r] = dp[l+1][r] + A[l]
                
                else:
                    dp[l][r] = max(dp[l][r],dp[l+1][r]+A[l],dp[l][r+1]+B[r])
            else:
                if l == len(A):
                    dp[l][r] = dp[l][r+1] #相手の番なので自分にはスコアが加算されない
                    
                elif r == len(B):
                    dp[l][r] = dp[l+1][r]
                    
                else:
                    dp[l][r] = min(dp[l][r+1],dp[l+1][r]) #自分の得点を最小にするように敵が動く
                    
                    
    print(dp[0][0]) #最初の状態からの先行の最大値
                    
    
if __name__ == '__main__':
    main()