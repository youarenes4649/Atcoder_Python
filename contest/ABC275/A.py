N=int(input())
H=list(map(int,input().split()))
ans=0
max_ans=0
for i in range(N):
    if max_ans<H[i]:
        max_ans=H[i]
        ans=i+1

print(ans)