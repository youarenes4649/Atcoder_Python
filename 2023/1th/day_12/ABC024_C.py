def main():
    N,D,K = map(int,input().split())
    LR = []
    for _ in range(D):
        l,r = map(int,input().split())
        LR.append([l,r])
        
    minzoku = []
    for _ in range(K):
        s,t = map(int,input().split())
        if s < t:
            for i in range(D):
                l,r = LR[i]
                if l <= t <= r and l <= s <= r:
                    minzoku.append(i+1)
                    break
                if l <= s <= r:
                    s = r
        else:
            for i in range(D):
                l,r = LR[i]
                if l <= t <= r and l <= s <= r:
                    minzoku.append(i+1)
                    break
                if l <= s <= r:
                    s = l          
    for a in minzoku:
        print(a)
                
            
        
if __name__ == '__main__':
    main()