A,B,C,D,E,F,X=map(int,input().split())

takahashi=0
aoki=0
tmp=X
while X>=0:
    
    X-=A
    if X<0:
        
        takahashi+=(X+A)*B
        
    else:
        
        takahashi+=A*B
        

        X-=C

X=tmp
while X>=0:
    X-=D
    if X<0:
        aoki+=(X+D)*E
        break
    else:
        aoki+=D*E

        X-=F

if takahashi==aoki:
    print('Draw')

elif takahashi>aoki:
    print('Takahashi')

else:
    print('Aoki')