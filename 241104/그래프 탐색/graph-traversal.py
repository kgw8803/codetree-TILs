# 인접 행렬
D1 = [
    [0 for _ in range(V+1)]
    for _ in range(V+1)
]

# 인접 리스트
D2 = [
    []
    for _ in range(V+1)
]

for _ in range(E):
    start end = map(int, input().split())
    # 인접 행렬
    D1[start][end] = 1

    #인접 리스트
    D2[start].append(end)


    #가중치가 있을 때
    # 인접 행렬
    D1[start][end] = cost

    #인접 리스트
    D2[start].append((end,cost))


# 주의할 점 중복 간선에서 가중치가 2개가 할당될 때

# ex) 1 2 10
      1 2 20 
# 문제 1에서 2로 가는 최단 거리를 구하세요.
    if D1[start][end] = -1 or D1[start][end] > cost:
        D1[start][end] = cost