
def main():
    import bisect
    N,M = map(int,input().split())
    X,Y = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    a,b = 0,0
    now = A[0]
    ans = 0
    while a < N and b < M:
        b = bisect.bisect_left(B,A[a] + X)
        now = A[a] + X
        if B[-1] < now:
            break
        ans += 1
        a = bisect.bisect_left(A,B[b] + Y)
        now = B[b] + Y
        if A[-1] < now:
            break
        
        
        
    print(ans)
        
        
        
        

if __name__ == '__main__':
    main()