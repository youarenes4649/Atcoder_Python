class UnionFind:
    def __init__(self, n):
        self.n=n
        self.parent_size=[-1]*n

    def merge(self, a, b):#a,bを同じグループとして記録
        x, y=self.leader(a), self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
        self.parent_size[x] += self.parent_size[y] 
        self.parent_size[y]=x
        return 

    def same(self, a, b):#a,bが同じグループならTrueを返す
        return self.leader(a) == self.leader(b)

    def leader(self, a):#aのリーダー（元の根を返す）
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]

    def size(self, a):#aが所属しているグループのサイズを返す
        return abs(self.parent_size[self.leader(a)])

    def groups(self):#groupをリストで返す
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

def main():
    N = int(input())
    uf = UnionFind(N)
    zahyou = []
    for i in range(N):
        x,y = map(int,input().split())
        zahyou.append((i,x,y))
        
    # xが一番近いやつとyが一番近いやつ２パターンある？
    edges = []
    zahyou.sort(key = lambda x : x[1])
    for n in range(N-1):
        i,xi,yi = zahyou[n]
        j,xj,yj = zahyou[n + 1]
        edges.append((abs(xi-xj),i,j))
    
    zahyou.sort(key = lambda x : x[2])
    print(zahyou)
    for n in range(N-1):
        i,xi,yi = zahyou[n]
    
        j,xj,yj = zahyou[n + 1]
        edges.append((abs(yi-yj),i,j))
        
    edges.sort()
    cost = 0
    
    for edge in edges:
        c,u,v = edge
        if not uf.same(u,v):
            cost += c
            uf.merge(u,v)
    
    print(cost)
            

    
        
    
                
    
        
    
        
    
        
    
        
        
        
if __name__ == '__main__':
    main()