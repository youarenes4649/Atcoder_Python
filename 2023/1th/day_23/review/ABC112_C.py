
def main():
    N = int(input())
    xyh = []
    for i in range(N):
        x,y,h = map(int,input().split())
        xyh.append((x,y,h))
        
    xyh.sort( key = lambda x: -x[2])
 
    for cx in range(100+1):
        for cy in range(100+1):
            H = set()
            for i in range(N):
                x,y,h = xyh[i]
                if h == 0:
                    continue
                Hi = abs(x-cx)+abs(y-cy) + h
                H.add(Hi)

            if len(H) == 1:
                
                ans = list(H)[0]
                ok = True
                for n in range(N):
                    if max(0,ans - abs(xyh[n][0]-cx) - abs(xyh[n][1]-cy)) != xyh[n][2]:
                        ok = False
                        
                if ok:
                    print(cx,cy,ans)
                    exit()  
                    
                
                    
                    
           
if __name__ == '__main__':
    main()