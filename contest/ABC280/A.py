H,W=map(int,input().split())
S=[]
ans=0
for i in range(H):
    s=input()
    ans+=s.count('#')

print(ans)
