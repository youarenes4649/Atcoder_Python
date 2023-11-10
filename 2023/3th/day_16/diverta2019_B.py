from collections import defaultdict
N = int(input())
D = defaultdict(int)

if N == 1:
  exit(print(1))

# 全頂点対を比較し(p,q)の候補を全列挙する
# 最も頻度が多い(p,q)にすればコストが最小化できる
S = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i == j: continue
    D[(S[i][0] - S[j][0], S[i][1] - S[j][1])] += 1 

print(N-max(D.values()))