H,W=map(int,input().split())
R,C=map(int,input().split())
if H==1 and W==1:
    print(0)
    exit()
if H==1:
    if C==1 or C==W:
        print(1)
        exit()
    else:
        print(2)
        exit()

if W==1:
    if R==1 or R==H:
        print(1)
        exit()

    else:
        print(2)
        exit()


if R==1 and C==1:
    print(2)
    exit()

elif R==1 and C==W:
    print(2)
    exit()

elif R==H and C==1:
    print(2)
    exit()

elif R==H and C==W:
    print(2)
    exit()

elif R==1 or R==H:
    print(3)
    exit()

elif C==1 or C==W:
    print(3)
    exit()

else:
    print(4)
    exit()



