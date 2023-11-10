import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
def prime_factorize(n):
    prime_list={}
    for i in range(2,n):
        if i*i >n:
            break

        cnt=0
        while n%i==0:
            cnt+=1
            n=n//i

        if cnt==0:

            continue
        prime_list[i]=cnt

    if n!=1:
        prime_list[n]=1

    return prime_list
def is_ok(x,p):
    return  p < x * (1 + x) // 2
    
def main():
    N = ii()
    if N == 1:
        print(0)
        exit()
    p_ls = prime_factorize(N)
    ans = 0
    for p in p_ls:
        ok = p_ls[p]
        ng = -1
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if is_ok(mid,p_ls[p]):
                ok = mid
            else:
                ng = mid
        if ok == 1:
            ans += 1
        else:
            ans += ok - 1
        
    print(ans)
        
if __name__ == '__main__':
    main()