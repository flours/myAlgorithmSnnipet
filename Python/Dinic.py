# Dinic's algorithm
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

def abc259g():
    H,W=map(int,input().split())
    f=[]
    for i in range(H):
        f+=list(map(int,input().split())),


    dinic=Dinic(H+W+2)

    base=0
    for i in range(H):
        s,a=0,0
        for j in f[i]:
            s+=abs(j)
            a+=j
        base+=s
        # 選ばない
        dinic.add_edge(0, i+1, s)
        # 選ぶ
        dinic.add_edge(i+1,H+W+1,s-a)

    for i in range(W):
        s,a=0,0
        for j in range(H):
            j=f[j][i]
            s+=abs(j)
            a+=j
        base+=s
        # 選ぶ
        dinic.add_edge(0, H+i+1, s-a)
        # 選ばない
        dinic.add_edge(H+i+1,H+W+1,s)

    for i in range(H):
        for j in range(W):
            if f[i][j]<0:
                dinic.add_edge(i+1,H+j+1,10**18)
            else:
                dinic.add_edge(i+1,H+j+1,f[i][j])

    print(base-dinic.flow(0,H+W+1))
abc259g()
