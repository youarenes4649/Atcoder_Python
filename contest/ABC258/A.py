K=int(input())
h=K//60
m=K%60

ans=21+h
ans2=m
if ans2<10:
    ans2='0'+str(ans2)

print(str(ans)+':'+str(ans2))