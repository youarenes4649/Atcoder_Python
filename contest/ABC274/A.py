A,B=map(int,input().split())
S=str(round(B/A,3))

if len(S)<4:
    num=4-len(S)
    for i in range(num+1):
        S+='0'


print(S)
#もしくは
print('{:.3f}'.format(B/A))