a,b,d=map(int,input().split())
import math
a_n=math.cos((d*math.pi)/180)*a-math.sin((d*math.pi)/180)*b
b_n=math.sin((d*math.pi)/180)*a+math.cos((d*math.pi)/180)*b

print(a_n,b_n)