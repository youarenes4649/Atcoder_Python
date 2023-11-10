# 二部グラフの問題　dfsを用いて未訪問から色を塗っていく
import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
class WeightedUnionFind:#差分制約とかがあった場合に使用できる 例ABC087D 
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]
    
def main():
        
    N,M = mi()
    A = li()
    B = li()
    UF = WeightedUnionFind(N)
    s = set() # (i,j) と(j,i)を同じものとして扱いたい

    for i in range(M):
        l = min(A[i]-1,B[i]-1)
        r = max(A[i]-1,B[i]-1)
        if UF.same(A[i]-1,B[i]-1) and (l,r) not in s:
            #既にあるけど0,1のペアになるやつの判定 diffが奇数ならok
            if UF.diff(A[i]-1,B[i]-1) % 2 == 0:
                #それ以外はNO
                print('No')
                exit()
        else:
            UF.union(A[i]-1,B[i]-1,1)
            s.add((l,r))

    print('Yes')


if __name__ == '__main__':
    main()