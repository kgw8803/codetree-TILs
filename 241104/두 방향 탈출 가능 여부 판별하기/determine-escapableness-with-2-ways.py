n, m = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n) 
]



def can_go(x,y):
    # 1. 격자 안에 있어야 함
    if x < 0 or x>= n or y < 0 or y>=m:
        return False

    # 2. 방문하지 않은 정점
    if visited[x][y]:
        return False


    # 3. 뱀이 있으면 안됨.
    if a[x][y] == 0:
        return False
    
    return True



def dfs(x, y):
    visited[x][y] = True

    dxy = [(1,0), (0,1)]
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny):
            dfs(nx, ny)




dfs(0,0)


if visited[-1][-1]:
    print(1)
else:
    print(0)