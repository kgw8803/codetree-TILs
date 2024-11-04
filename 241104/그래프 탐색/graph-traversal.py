N, M = map(int, input().split())

graph = [ [] for _ in range(N+1)]


for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [False] * (N+1)


def dfs(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)

cnt = 0
for v in visited[2:]:
    if v:
        cnt += 1

print(cnt)