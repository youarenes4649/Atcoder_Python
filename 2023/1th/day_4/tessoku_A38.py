
def main():
    from itertools import accumulate
    from collections import defaultdict
    cnt = defaultdict(int)
    D,N = map(int,input().split())
    day = [[24]*D for _ in range(N)]
    day_cum = []
    for i in range(N):
        l,r,h = map(int,input().split())
        l -= 1
        r -= 1
        for j in range(l,r+1):
            day[i][j] = h
        day_cum.append(day[i])
    ans = [25]*(D)
    for i in range(D):
        for j in range(N):
            ans[i] = min(ans[i],day_cum[j][i])
    print(sum(ans))        
        
        

    
        
    
    
if __name__ == '__main__':
    main()