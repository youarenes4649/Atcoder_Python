
def main():
    from itertools import accumulate
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    flag = [False]*(N)
    for i in range(N):
        if A[i]*2 >= A[-1]:
            flag[i] = True
    A_cum = list(accumulate(A))
   
    ans = 0
    for i in range(N-1,-1,-1):
        if flag[i] == True:
            ans += 1
            continue
        if  flag[i+1] == True and A_cum[i]*2 >= A[i+1]:
            flag[i] = True
            ans += 1
    
    print(ans)
    
    
        
            
        
if __name__ == '__main__':
    main()