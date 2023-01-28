#どんなに大きくても１５桁までしかないから全探索
def main():
    def inter(N,l,r):
        r = min(r,N)
        return max(0 ,r - l + 1)
    
    N = int(input())
    ans = 0 
    for i in range(1,16):#先頭に 1 が i個
        for j in range(16):
            l = '1' * i + '0' * j
            r = '1' * i + '9' * j
            
            ans += inter(N,int(l),int(r))
    
    print(ans)
            
            
             
    

        
    
    
if __name__ == '__main__':
    main()