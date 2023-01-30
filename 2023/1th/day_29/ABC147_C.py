def main():
    N = int(input())
    people = [[]*N for _ in range(N)]
    for i in range(N):
        A = int(input())
        for j in range(A):
            x,y = map(int,input().split())
            people[i].append((x-1,y))
    ans = 0  
    for i in range(1<<N):
        honest = []
        for j in range(N):
            if (i >> j) & 1 == 1:
                honest.append(j)
        
        check = True
        for n in range(N):
            if n not in honest:
                continue
            for per in people[n]:
                if per[1] == 1: 
                    if per[0] not in honest:
                        check = False
                    
                else:
                    if per[0] in honest:
                        check = False
                
        if check:
            ans = max(ans,len(honest))
            
    print(ans)
            
                        
        
if __name__ == '__main__':
    main()