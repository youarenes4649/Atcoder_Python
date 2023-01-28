K = int(input())
amari = 0

for i in range(1, K+1):
  amari = amari*10 + 7
  if amari%K==0:
    print(i)
    exit()
    
  amari %= K
    
print(-1)