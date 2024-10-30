N = int(input())
visited = [False] * (N+1)
arr = []

def f(curr_num):
    if curr_num == N + 1:
        print(*arr)
        return 


    for i in range(1, N + 1):
        if visited[i]:
            continue

        visited[i] = True
        arr.append(i)

        f(curr_num + 1)

        visited[i] = False
        arr.pop()




f(1)