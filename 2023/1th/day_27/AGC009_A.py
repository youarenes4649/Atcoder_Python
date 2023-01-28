
def main():
    N = int(input())
    A = []
    B = []
    #下から見ていけばいい
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
        
    A = A[::-1]
    B = B[::-1]
    
    ans = 0
    for i in range(N):
        a,b = A[i],B[i]
        ans += ((a + (b - 1))//b) * b - a
        if i + 1 < N :
            A[i+1] += ans
        
    print(ans)
        
if __name__ == '__main__':
    main()