
def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        ans = 0
        s = []
        now = 0
        while now+i < N:
            if S[now] != S[now+i]:
                ans += 1
                
            else:
                break
            now += 1
        print(ans)
        
                
        
            
if __name__ == '__main__':
    main()