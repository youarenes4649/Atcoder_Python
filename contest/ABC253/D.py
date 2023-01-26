N,A,B=map(int,input().split())
from math import gcd
total=N*(1+N)//2
def lcm(a,b):
    return a*b//gcd(a,b)
LCM=lcm(A,B)
range_A=N//A
range_B=N//B
range_LCM=N//LCM
total-=A*(range_A)*(1+range_A)//2
total-=B*(range_B)*(1+range_B)//2
total+=LCM*(range_LCM)*(1+range_LCM)//2
print(total)
    
    