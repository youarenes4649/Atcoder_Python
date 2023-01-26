def main():
    N = int(input())
    LR = []
    for _ in range(N):
        l,r = map(int,input().split())
        LR.append([r,l])
        
    LR.sort()
    i = 1
    ans = 0
    end = LR[0][1]
    
    while i < len(LR):
        if end <= LR[i][0]: #見れる時
            end = LR[i][1]
            ans += 1
        i += 1
    print(ans)
            
                   
        
if __name__ == '__main__':
    main()