def main():
    def check(m):
        R = S[m:]
        len_r = len(R)
        cnt = 0
        i, j = 0, 0
        while i < len(T) and j < len_r:
            if T[i] == R[j]:
                j += 1 
            i += 1
            
        return j == len_r
                
        
    N = int(input())
    S = input()
    T = input()
    if sorted(S) != sorted(T):
        print(-1)
        exit()
    
    ok = N
    ng = -1
    
    while ok - ng > 1:
        mid = (ok + ng)//2
        
        if check(mid):
            ok = mid
        
        else:
            ng = mid
            
    print(ok)
    
        
    
if __name__ == '__main__':
    main()