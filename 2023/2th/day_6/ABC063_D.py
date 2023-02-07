
def main():
    def check(x):
        C = A - B
        HH = [h - B * x for h in H if h - B*x > 0 ]
        cnt = 0
        for hh in HH:
            cnt += (hh + C - 1) // C
        
        if cnt <= x:
            return True
        else:
            return False
    
    N,A,B = map(int,input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    
    ok = 10 ** 9
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
            
            
    print(ok)
if __name__ == '__main__':
    main()