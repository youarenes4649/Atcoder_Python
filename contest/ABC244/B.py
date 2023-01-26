N=int(input())
T=input()
now=[0,0]
cnt=0
for t in T:
    if t=='R':
        cnt+=1
        continue

    if cnt%4==0:#東
        now[0]+=1

    elif cnt%4==1:
        now[1]-=1

    elif cnt%4==2:
        now[0]-=1

    else:
        now[1]+=1

print(*now)
    



