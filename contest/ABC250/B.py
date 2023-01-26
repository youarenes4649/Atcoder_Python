N,A,B=map(int,input().split())

grid=[['.']*B ]
if N==1:
    ans=''
    for g in grid:
        ans+=''.join(g)

    for a in range(A):
        print(ans)


    exit()

    
grid.append(['#']*B)
grid_rev=[['#']*B]
grid_rev.append(['.']*B)
for i in range(N-2):
    if i%2==0:

        grid.append(['.']*B)
        grid_rev.append(['#']*B)
    else:
        grid.append(['#']*B)
        grid_rev.append(['.']*B)

ans=''
ans2=''
for g in grid:
    ans+=''.join(g)

for gr in grid_rev:
    ans2+=''.join(gr)

while N>0:
    for a in range(A):
        print(ans)
    N-=1
    if N==0:
        exit()

    for a in range(A):
        print(ans2)
    N-=1






