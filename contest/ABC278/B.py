H,M=map(int,input().split())
def change(H,M):
    if len(str(H))==1:
        A=0
        B=int(str(H)[0])
    else:
        A=int(str(H)[0])
        B=int(str(H)[1])


    if len(str(M))==1:
        C=0
        D=int(str(M)[0])
    else:
        C=int(str(M)[0])
        D=int(str(M)[1])

    return A,B,C,D
for h in range(H,24):
    for m in range(0,60):
        if h==H:
            if m<M:
                continue

        a,b,c,d=change(h,m)
        tmp=b
        b=c
        c=tmp
        new_H=10*a+b
        new_D=10*c+d
        if 0<=new_H<=23 and 0<=new_D<=59:
            print(h,m)
            exit()
for h in range(0,H):
    for m in range(0,60):
        if h==H:
            if m<M:
                continue

        a,b,c,d=change(h,m)
        tmp=b
        b=c
        c=tmp
        new_H=10*a+b
        new_D=10*c+d
        if 0<=new_H<=23 and 0<=new_D<=59:
            print(h,m)
            exit()



