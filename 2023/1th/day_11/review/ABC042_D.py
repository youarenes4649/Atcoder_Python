
def main():
    mod = 10**9+7
    H,W,A,B = map(int,input().split())
    fact = [[] for _ in range(H+W-2)]
    inv = [[] for _ in range(H+W-2)]
    fact[0] = 1
    inv[0] = 1
    ans = 0
    
    for i in range(1,H+W-2):
        fact[i] = fact[i-1]*i%mod
        inv[i] = pow(fact[i],10**9+5,mod)
        
    for i in range(B,W):
        ans += fact[H-A-1+i]*inv[H-A-1]*inv[i]*fact[A-1+W-1-i]*inv[W-1-i]*inv[A-1]
        ans %= mod
        
    print(ans)
        
        
    
if __name__ == '__main__':
    main()