
def main():
    N,C = map(int,input().split())
    event = []
    for i in range(N):
        a,b,c = map(int,input().split())
        event.append([a,c])
        event.append([b+1,-c])
    event.sort(reverse=True)
    cost = 0
    day = 0
    ans = 0
    while len(event) > 0:
        t,fee = event.pop()
        if day != t:
            ans += min(C,cost)*(t-day)
        
        day = t
        cost += fee
    
    
    
        
        
        
        
    print(ans)
            
            
if __name__ == '__main__':
    main()