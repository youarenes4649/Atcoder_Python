from sys import stdin
def input():
    return stdin.readline().rstrip()
class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1 for i in range(n)]
        self.rank = [1 for i in range(n)]
        # self.member = [set([i]) for i in range(n)]
        self.leaders = set(range(n))
        """代表元の集合
        """
 
    def find(self, x: int) -> int:
        """x が属する集合の代表元
 
        Args:
            x (int): 0-indexed
 
        Returns:
            int: 代表元
        """
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def unite(self, x: int, y: int) -> int:
        """x, y が属する集合を合併
 
        Args:
            x (int): 0-indexed
            y (int): 0-indexed
 
        Returns:
            int: 減少した集合数
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        # x を新しい親に
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.leaders.discard(y)
        # self.member[x] |= self.member[y]
        return 1
 
    def same(self, x: int, y: int) -> bool:
        """x と y が同じ集合に属するか
 
        Args:
            x (int): 0-indexed
            y (int): 0-indexed
 
        Returns:
            bool: 同じ集合に属するか
        """
        return self.find(x) == self.find(y)
 
    def size(self, x: int) -> int:
        """x が属する集合の要素数
 
        Args:
            x (int): 0-indexed
 
        Returns:
            int: 要素数
        """
        x = self.find(x)
        return -(self.parent[x])
 
    def group_num(self) -> int:
        """全体の集合数
 
        Returns:
            int: 集合の数
        """
        return len(self.leaders)
 
    def all_members(self):
        """全集合の列挙
 
        Returns:
            Generator[set[int], None, None]: 集合たち(0-indexed)
        Note:
            self.memberを有効にせよ
        """
        member = self.member
        return (member[i] for i in self.leaders)
 
 
n = int(input())
po = [tuple(map(int, input().split())) for i in range(n)]
pod = {(x, y): i for i, (x, y) in enumerate(po)}#この組に属するものはこの数字という感じでナンバーを配布　典型９０にもあるので復習

uf = UnionFind(n)
dxyl = [(-1, -1), (-1, 0), (0, -1), (0, +1), (+1, 0), (+1, +1)]
for i, (x, y) in enumerate(po):
    for dx, dy in dxyl:
        nx, ny = x + dx, y + dy
        if (nx, ny) in pod:
            uf.unite(i, pod[nx, ny])#iが元の黒く塗られている部分でそれとそれに近いものをunite   する
            
ans = uf.group_num()
print(ans)
