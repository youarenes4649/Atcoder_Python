A,B,C,D,E,F=map(int,input().split())
mod=998244353
a=A*B*C
a%=mod
b=D*E*F
b%=mod
print((a-b)%mod)