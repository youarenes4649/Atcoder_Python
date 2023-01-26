A,B,C,D=map(int,input().split())

if A==0 and B==0 and C==23 and D==59:
    print('Takahashi')
    exit()
if A<C:
    print('Takahashi')
    exit()

elif A>C:
    print('Aoki')
    exit()

else:
    if B<=D:
        print('Takahashi')
        exit()

    else:
        print('Aoki')
        exit()

