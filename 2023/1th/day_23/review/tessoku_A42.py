
def main():
    N,K = map(int,input().split())
    AB = []
    for _ in range(N):
        a,b = map(int,input().split())
        AB.append((a,b))
    mans = 0
    for a in range(100):
        for b in range(100):
            ans = 0
            for n in range(N):
                if a <= AB[n][0] <= a+K and b <= AB[n][1] <= b+K:
                    ans += 1
                    
            mans = max(mans,ans)
            
    print(mans)
                    
            
                
if __name__ == '__main__':
    main()