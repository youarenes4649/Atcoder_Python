def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    mod = 998244353
    ans = 0
    tmp = 0 #最初にAi**(i-2)+...を求めておく　ここから引く
    for i,a in enumerate(A):
        ans += a**2
        if i == 0:
            continue
        tmp += a*(2**(i-1))
        
    
    for i in range(1,N):
        ai = A[i-1]
        ans += ai * tmp
        ans %= mod
        tmp -= A[i]
        tmp = tmp/2
        tmp %= mod
        
    print((ans)%mod)
            
    
if __name__ == '__main__':
    main()