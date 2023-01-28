def main():
    N,M = map(int,input().split())
    S = []
    T = []
    for i in range(N):
        s = input()[3:]
        S.append(s)
    
    for i in range(M):
        t = input()
        T.append(t)
    ans = 0
    for s in S:
        if s in T:
            ans += 1
            
    print(ans)
            
        
if __name__ == '__main__':
    main()