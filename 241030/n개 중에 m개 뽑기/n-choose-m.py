N, M = map(int, input().split())
arr = []

# 0 혹은 1의 값이 있는데, 
# 1이 있는 위치의 index를 출력

def print_arr():
    for i in range(N):
        if arr[i] == 1:
            print(i+1, end=" ")
    print()



def f(curr_num, cnt):
    if curr_num == N+1:
        # 출력 -> 1의 개수가 M개면,
        if cnt == M:
            print_arr()

        return

    for i in range(1,-1,-1):
        arr.append(i)
        f(curr_num + 1, cnt + i)
        arr.pop()


f(1,0)