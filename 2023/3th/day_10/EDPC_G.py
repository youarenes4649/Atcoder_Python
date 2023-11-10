from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N)]
d = [0]*N

# グラフの出入のノードの番号を読み取り、各ノードの行先をGにリスト化
# 同時に入次数dをカウント
for i in range(M):
    x, y = map(int, input().split())
    G[x-1].append(y-1)
    d[y-1] += 1

# 入次数が0のノードに隣接するノードをセットに追加
checklist = []
length = 0
for i in range(len(d)):
    if d[i]==0:
        checklist.append(i)

# 入次数が0のノードに隣接するノードの入次数を-1
# 入次数が0になったら次のノードリストに追加
# すべての入次数が0になるまで繰り返す
while len(checklist)>0:
    nextlist = []
    for i in checklist:
        for j in G[i]:
            d[j] -= 1
            if d[j] == 0:
                nextlist.append(j)
    checklist = nextlist.copy()
    length += 1 

# 辺の数を出力
print(length-1)