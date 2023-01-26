def yakusu(n):#少し遅い
    res=set()
    i=1
    while i*i<=n:
        if n%i==0:
            res.add(i)

            res.add(n//i)
            
        i+=1
    res.add(n)
    return res


def main():
    N,M = map(int,input().split())
    p_ls = list(yakusu(M))
    p_ls.sort()
    ans = 1
    for p in p_ls:
        if p * N <= M:
            ans = p
            
    print(ans)
    

if __name__ == '__main__':
    main()