
def main():
    N = int(input())
    AB = []
    for _ in range(N):
        a,b = map(int,input().split())
        AB.append((a,b))
    ans = 0
    for i in range(4):
        tmp_ans = 0
        for j in range(N):
            a,b = AB[j]
            if i == 0:#正 + 正
                if a + b > 0:
                    tmp_ans += a + b
                    
            if i == 1:
                if a - b > 0:
                    tmp_ans += a - b
                    
            if i == 2:
                if - a + b > 0:
                    tmp_ans += b - a
            
            if i == 3:
                if - (a + b) > 0:
                    tmp_ans -= a + b
                    
            
            ans = max(ans,tmp_ans)
            
    print(ans)
                    
                    
            
                    
                
            
            
    
if __name__ == '__main__':
    main()