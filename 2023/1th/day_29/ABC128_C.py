
def main():
    N,M = map(int,input().split())
    S = [list(map(int,input().split()))[1:] for _ in range(M)]
    P = list(map(int,input().split()))
    ans = 0
    for i in range(1<<N):
        use = [] # onにするスイッチ
        for j in range(N):
            if (i>>j) & 1 == 1:
                use.append(j+1)
        
        check = True
        for k in range(M):
            cnt = 0
            for sw in use:
                if sw  in S[k]:
                    cnt += 1
                    
            if cnt % 2 != P[k]:
                check = False
                
                
        if check:
            ans += 1
        
        
    print(ans)
                    
                    
                 
                
        
                
                
                
        
                
if __name__ == '__main__':
    main()