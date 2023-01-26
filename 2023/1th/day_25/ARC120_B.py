
def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    mod = 998244353
    ans = 1
    for i in range(H+W-1):#マンハッタン距離がある定数の時,その定数を満たすますの通り方は１順路につき1通り
        red = False
        blue = False
        for j in range(W):
            if i - j < 0 or i - j >= H:
                continue
            
            if S[i-j][j] == 'R':
                red = True
                
            if S[i-j][j] == 'B':
                blue = True
                
        if red and blue:
            print(0)
            exit()
            
        if red == True and blue == False:
            ans *= 1
            ans %= mod
        if red == False and blue == True:
            ans *= 1
            ans %= mod
            
        if red == False and blue == False:
            ans *= 2
            ans %= mod
            
    print(ans)
            
            
        
            
        
    
if __name__ == '__main__':
    main()