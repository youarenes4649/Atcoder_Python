from collections import Counter
import math
s = input()
c = Counter(s)

odd = 0
even = 0
for val in c.values():
  if val % 2 == 0:
    even += val
  else:
    odd += 1
    even += val-1

if odd == 0:
  print(even)
else:
  print(1 + 2 * ((len(s)-odd) // (2*odd)))