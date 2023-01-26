
def main():
    N = int(input())
    from copy import deepcopy
    from math import gcd
    cnt = 0
    ans = set([6,10,15])
    for i in range(2,10000):
        if 6*i <= 10000:
            ans.add(6*i)
        if 10*i <= 10000:
            ans.add(10*i)        
        if 15*i <= 10000:
            ans.add(15*i)     
            
        if len(ans) > N:
            print(*list(ans)[:N])
                
    
            
        
        
if __name__ == '__main__':
    main()