#2つ解法で解いてみる

N=int(input())

A=list(map(int,input().split()))
max_a=max(A)
count=[0]*(max_a+1)
ans=0
def yakusu(n):
    res=set()
    i=1
    while i*i<=n:
        if n%i==0:
            res.add(i)
            res.add(n//i)
        i+=1
    return res

for a in A:
    count[a]+=1
for a in set(A):
    for i in yakusu(a):
        ans+=count[i]*count[a]*count[a//i]

print(ans)
             
