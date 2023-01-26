N=int(input())
a=hex(N)
from collections import defaultdict
port=defaultdict(str)
if len(a)==3:
    a='0'+a[2:]
else:
    a=a[2:]
print(a.upper())