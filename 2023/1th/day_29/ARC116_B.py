def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    ans = 0
    total = 0
    A.sort()
    for a in A: #例外
        ans += a**2
   
    for i,a in enumerate(A):
        if i == 0:
            continue
        total += a * pow(2,i-1,mod)
        total %= mod


    for i in range(N-1):
        ans += A[i] * total
        ans %= mod
        total -= A[i+1]
        total -= total//2
        total %= mod
        
    print(ans%mod)
        
    
if __name__ == '__main__':
    main()