import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import defaultdict, deque, Counter
import copy
from itertools import combinations, permutations, product, accumulate
from heapq import heapify, heappop, heappush
import math
import bisect
import sys
# sys.setrecursionlimit(700000)
input = lambda: sys.stdin.readline().rstrip('\n')
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y)

class segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size
        self.d[p]=x
        for i in range(1,self.log+1):
            self.update(p>>i)
    def get(self,p):
        assert 0<=p and p<self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
            if (l&1):
                sml=self.op(sml,self.d[l])
                l+=1
            if (r&1):
                smr=self.op(self.d[r-1],smr)
                r-=1
            l>>=1
            r>>=1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def max_right(self,l,f):
        assert 0<=l and l<=self.n
        assert f(self.e)
        if l==self.n:
            return self.n
        l+=self.size
        sm=self.e
        while(1):
            while(l%2==0):
                l>>=1
            if not(f(self.op(sm,self.d[l]))):
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l])):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:
                break
        return self.n
    def min_left(self,r,f):
        assert 0<=r and r<self.n
        assert f(self.e)
        if r==0:
            return 0
        r+=self.size
        sm=self.e
        while(1):
            r-=1
            while(r>1 & (r%2)):
                r>>=1
            if not(f(self.op(self.d[r],sm))):
                while(r<self.size):
                    r=(2*r+1)
                    if f(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r& -r)==r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])

class EulerTour():

    def __init__(self, N, root=0) -> None:
        self.N = N
        self.root = root
        self.adj = [[] for _ in range(N)]
        self.parent = [None]*N
        self.depth = [inf]*(N+1)
        self.visit = [None]*N #in
        self.leave = [None]*N #out
    
    def add_edge(self, u, v, w=1):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])
    
    def tour(self):
        V = []
        E = []
        stack = [(None, self.root, 0)]
        while stack: #
            pre, now, w = stack.pop()
            if now >= 0:
                if pre is None: self.depth[now] = 0
                else: self.depth[now] = self.depth[pre]+1
                if pre is not None: self.parent[now] = pre
                self.visit[now] = len(V)
                V.append(now)
                E.append(w)
                self.leave[now]= len(V)
                for next, w in self.adj[now]:
                    if next == pre: continue
                    stack.append((next, ~now, -w))
                    stack.append((now, next, w))
            else:
                now = ~now
                V.append(now)
                E.append(w)
                self.leave[now] = len(V)

    ## この範囲はセグ木を使うので、必要なければコメントアウト ##
        def op(u, v):
            if self.depth[u] <= self.depth[v]: return u
            else: return v
        self.depth_min = segtree(V, op, self.N)
        self.rv_path = segtree(E, lambda u, v: u+v, 0)
    
    def lca(self, u, v):
        if self.visit[u] > self.visit[v]: u, v = v, u
        return self.depth_min.prod(self.visit[u], self.leave[v])

    def dist(self, u, v): #u,v間のパスを出力
        a = self.lca(u, v)
        return self.rv_path.prod(0, self.leave[u])+self.rv_path.prod(0, self.leave[v])-2*self.rv_path.prod(0, self.leave[a])
    
    def update_parent_edge(self, v, w): # vとその親を繋ぐ辺の重みをwに更新
        self.rv_path.set(self.visit[v], w)
        self.rv_path.set(self.leave[v], -w)
    #########################################################
    
    def is_ancestor(self, p, s): # pはsの祖先か？
        return self.visit[p] <= self.visit[s] < self.leave[p]

def main():
    N = ii()
    et = EulerTour(N)
    edge = []
    for _ in range(N - 1):
        x,y = mi()
        x -= 1
        y -= 1
        edge.append((x, y))
        et.add_edge(x, y)
    et.tour()
    Q = ii()
    for _ in range(Q):
        a,b = mi()
        print(et.dist(a - 1,b - 1) + 1)
        
if __name__ == '__main__':
    main()