import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
class UnionFind: #所属している場所の辺数も記録できる
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
    self.edges = [0] * n

  def get_parent(self, x):
    if self.parents[x] < 0:
      return x
    self.parents[x] = self.get_parent(self.parents[x])
    return self.parents[x]
  
  def get_size(self, x):
    return -self.parents[x]
  
  def unite(self, x, y):
    x = self.get_parent(x)
    y = self.get_parent(y)
    if x == y:
      self.edges[x] += 1
      return
    self.edges[x] += self.edges[y]
    self.edges[x] += 1
    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def same(self, x, y):
    return self.get_parent(x) == self.get_parent(y)
  

def main():
    N,M = mi()
    UF = UnionFind(N)
    for _ in range(M):
        u,v = mi()
        u -= 1
        v -= 1
        UF.unite(u,v)
    for i in range(N):
        if i == UF.get_parent(i):
            if UF.edges[i] != UF.get_size(i):
                print('No')
                exit()
    print('Yes')
                
if __name__ == '__main__':
    main()