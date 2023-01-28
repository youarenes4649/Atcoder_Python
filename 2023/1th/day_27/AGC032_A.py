
def main():
    from collections import deque
    N = int(input())
    B = list(map(int,input().split()))
    
    ans = []
    for j in range(N):
        for i in range(N,0,-1):
            if i > len(B):
                continue
            if B[i-1] == i:
                ans.append(i)
                B = B[:i-1] + B[i:]
            
                break
    if len(ans) == N:
        for a in ans[::-1]:
            print(a)
   
    else:
        print(-1)
            
    
        
        
        
    

    
                
        
if __name__ == '__main__':
    main()