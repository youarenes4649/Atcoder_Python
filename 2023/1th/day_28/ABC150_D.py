
def main():
    from math import gcd
    def lcm(a,b) :
        return a*b//(gcd(a,b))
    
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    M = M * 2
    LCM = A[0]
    for a in A:
        LCM = lcm(LCM,a)
    
    if LCM > M:
        print(0)
    else:
        now = LCM//2
        M //= 2
        M -= now
        ans = (M+ LCM-1)//LCM
        print(ans)
            
   
   
    
    
    
    
if __name__ == '__main__':
    main()