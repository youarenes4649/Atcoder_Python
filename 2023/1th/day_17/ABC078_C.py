
def main():
    from itertools import accumulate
    import bisect
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    X = 0
    A_sum = sum(A)
    #山の上からとるから　...
    ans = 10*20
    for i in range(N-1):
        X += A[i]
        ans = min(ans,abs(A_sum - 2*X))
        
    print(ans)
        
if __name__ == '__main__':
    main()