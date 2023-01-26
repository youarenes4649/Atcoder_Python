
def main():
    N,P,Q,R,S = map(int,input().split())
    P-=1
    R-=1
    A = list(map(int,input().split()))
    A[P:Q] , A[R:S] = A[R:S],A[P:Q]
    print(*A)
if __name__ == '__main__':
    main()