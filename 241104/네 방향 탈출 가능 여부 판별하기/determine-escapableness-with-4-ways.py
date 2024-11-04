from collections import deque

N, M = map(int, input().split())

A = [
    list(map(int, input().split()))
    for _ in range(N)
]

visited = [
    [False for _ in range(M)]
    for _ in range(N)
]



def can_go(x, y):
    if x < 0 or x >= N or y < 0 or  y >= N:
        return False
    if visited[x][y] or A[x][y] == 0:
        return False
    return True



dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]



def bfs():
    q = deque()

    q.append((0,0))
    visited[0][0] = True


    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True


bfs()


if visited[-1][-1]:
    print(1)
else:
    print(0)