def dfs(A):
  if len(A)==N:
    print(*A)
    return
  if len(A)==0: start=1
  else: start=A[-1]+1# 
  for i in range(start,M+1):
    print(A+[i])
    dfs(A+[i])
 
N,M=map(int,input().split())
dfs([])

def dfs(A):
  if len(A)==N:
    print(*A)
    return 

  if len(A)==0:
    start=1
  else:
    start=A[-1]+1

    for i in range(start,M+1):
      dfs(A+[i])#最初Aには何も入ってないので1,2,3が先頭のやつが入る
      #そこから処理は１から順番に行っていく
