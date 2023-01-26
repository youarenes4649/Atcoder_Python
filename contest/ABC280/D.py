K=int(input())

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

#print(prime_factorize(2020)) -->{2: 2, 5: 1, 101: 1}

p_ls=prime_factorize(K)

#n! を割り切れる回数
def legendre(n,p):
    res=0
    p2=p
    while True:
        tmp=n//p2

        if tmp==0:
            break
        res+=tmp
        p2*=p

    return res

def judge(m):
    for p in p_ls:
        if legendre(m,p)<p_ls[p]:
            return False
    return True



ok=K
ng=1
while ok-ng>1:
    mid=(ok+ng)//2

    if judge(mid):
        ok=mid
    else:
        ng=mid
print(ok)