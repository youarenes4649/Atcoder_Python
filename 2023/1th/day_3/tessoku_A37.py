
def main():
    N,M,B = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    ans = B*(N*M)
    for i in range(N):
        ans += A[i]*M
    for j in range(M):
        ans += C[j]*N
    print(ans)
if __name__ == '__main__':
    main()