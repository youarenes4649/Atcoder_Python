s1,s2,s3=map(str,input().split())
t1,t2,t3=map(str,input().split())


cnt=0
if s1==t1:
    cnt+=1

if s2==t2:
    cnt+=1

if s3==t3:
    cnt+=1

if cnt%3==1:
    print('No')

else:
    print('Yes')