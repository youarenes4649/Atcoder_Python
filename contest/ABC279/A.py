S=input()
cnt=[0]*2
for s in S:
    if s=='w':
        cnt[0]+=1

    else:
        cnt[1]+=1

ans=cnt[0]*2+cnt[1]
print(ans)