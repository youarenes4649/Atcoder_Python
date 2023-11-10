class UnionFind:
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
  

n, m = map(int, input().split()) 
uf = UnionFind(n)
for i in range(m):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  uf.unite(u, v)

for i in range(n):
  if uf.parents[i] < 0: #リーダーのペアレントはマイナスになっている
    if uf.parents[i] != -uf.edges[i]:
      print('No')
      break
else:
  print('Yes')