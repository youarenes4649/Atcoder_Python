
def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(N-1):
        if A[i+1]< A[i]:
            ans[i] = 1
            ans[i+1] ^= ans[i]
            
    print(*ans)
        
if __name__ == '__main__':
    main()