
def main():
    N,A,B,C = map(int,input().split())
    take = []
    for i in range(N):
        l = int(input())
        take.append(l)
        
    ans = [0]
    #竹をどのやつに合わせるか
    def dfs(x,a,b,c):
        if x == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a,b,c) > 0 else 10**9 
        ret0 = dfs(x + 1 , a , b , c)
        ret1 = dfs(x + 1 , a + take[x], b , c) + 10
        ret2 = dfs(x + 1 , a , b + take[x] , c) + 10
        ret3 = dfs(x + 1 , a , b , c + take[x]) + 10
        
        return min(ret0,ret1,ret2,ret3)
    
    
    print(dfs(0,0,0,0))
        
        
        
        
        
    
        
    
if __name__ == '__main__':
    main()