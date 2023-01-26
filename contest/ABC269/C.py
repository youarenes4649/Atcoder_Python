N=int(input())
bin=format(N,'b')
array=[]
import itertools
for i,b in enumerate(str(bin)):
    if b=='1':
        array.append([1,0])
    else:
        array.append([0])
ans=list(itertools.product(*array))
anss=[]
for a in ans:
    an=''
    for i in a:
        an+=str(i)

    anss.append(int(an,2))

anss.sort()
for a in anss:
    print(a)




