def main():
    import bisect
    X = [1,2,3,4,5]
    idx = bisect.bisect_left(X,5)
    print(idx)
    N = int(input())
    rdog = []
    gdog = []
    bdog = []
    for i in range(2*N):
        a,c = map(str,input().split())
        if c == 'R':
            rdog.append(int(a))
        if c == 'G':
            gdog.append(int(a))
        if c == 'B':
            bdog.append(int(a))
    rdog.sort()
    gdog.sort()
    bdog.sort()
    R = len(rdog)
    G = len(gdog)
    B = len(bdog)
    
    if R%2 == 0 and G%2 == 0 and B%2 == 0:
        print(0)
        exit()
    a,b,c = 0,0,0 #aは偶数　b,cは奇数
    if R%2 == 0:
        a,b,c = rdog,gdog,bdog
        
    if G%2 == 0:
        a,b,c = gdog,rdog,bdog
    
    if B%2 == 0:
        a,b,c = bdog,rdog,gdog
    
    ans1, ans2,ans3 = 10**20, 10**20,10**20
    for i in range(len(b)):
        dog = b[i]
        idx = bisect.bisect_left(c,dog)
        if idx == len(c):
            ans1 = min(ans1,abs(c[idx-1]-dog))
            
        elif idx == 0:
            ans1 = min(ans1,abs(c[idx]-dog))
        
        elif idx == len(c)-1 :
            ans1 = min(ans1,abs(c[idx]-dog),abs(c[idx-1]-dog))
        
        else:
            ans1 = min(ans1,abs(c[idx]-dog),abs(c[idx-1]-dog),abs(c[idx+1]-dog))
    
    for i in range(len(b)):
        dog = b[i]
        idx = bisect.bisect_left(a,dog)
        if len(a) == 0:
            continue
        if idx == len(a) :
            ans1 = min(ans1,abs(a[idx-1]-dog))
            
        elif idx == 0:
            ans1 = min(ans1,abs(a[idx]-dog))
        
        elif idx == len(a)-1 :
            ans1 = min(ans1,abs(a[idx]-dog),abs(a[idx-1]-dog))
        
        else:
            ans1 = min(ans1,abs(a[idx]-dog),abs(a[idx-1]-dog),abs(a[idx+1]-dog))
        
    for i in range(len(b)):
        dog = b[i]
        idx = bisect.bisect_left(a,dog)
        if len(a) == 0:
            continue
        if idx == len(a) and len(a) != 0:
            ans2 = min(ans2,abs(a[idx-1]-dog))
            
        elif idx == 0:
            ans2 = min(ans2,abs(a[idx]-dog))
        
        elif idx == len(a)-1 :
            ans2 = min(ans2,abs(a[idx]-dog),abs(a[idx-1]-dog))
        
        else:
            ans2 = min(ans2,abs(a[idx]-dog),abs(a[idx-1]-dog),abs(a[idx+1]-dog)) 
    for i in range(len(c)):
        dog = c[i]
        idx = bisect.bisect_left(a,dog)
        if len(a) == 0:
            continue        
        if idx == len(a):
            ans3 = min(ans3,abs(a[idx-1]-dog))
            
        elif idx == 0:
            ans3 = min(ans3,abs(a[idx]-dog))
        
        elif idx == len(a)-1 :
            ans3 = min(ans3,abs(a[idx]-dog),abs(a[idx-1]-dog))
        
        else:
            ans3 = min(ans3,abs(a[idx]-dog),abs(a[idx-1]-dog),abs(a[idx+1]-dog)) 
            
    print(min(ans1,ans2+ans3))
            
        
        
    
if __name__ == '__main__':
    main()