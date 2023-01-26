A,B=map(int,input().split())
import math
d=math.sqrt(A**2+B**2)

x=A/d
y=B/d
ans=[x,y]

print(*ans)
