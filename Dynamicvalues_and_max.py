import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solve():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        g = [[] for _ in range(n)]
        for _ in range(n-1):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
        
        depth = [0]*n
        subtree = [0]*n
        
        def dfs(u, p):
            subtree[u] = 1
            for v in g[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                dfs(v, u)
                subtree[u] += subtree[v]
        
        dfs(0, -1)
        
        gain = []
        for i in range(n):
            gain.append(depth[i] - (subtree[i] - 1))
        
        gain.sort(reverse=True)
        
        print(sum(gain[:k]))

solve()