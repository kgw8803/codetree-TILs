K, N = map(int, input().split())
arr = []

def print_answer():
    for elem in arr:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == N + 1:
        print_answer()
        return

    for i in range(1, K+1):
        if len(arr) >= 2 and arr[-1] == i and arr[-2] == i:
            continue

        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

    return

choose(1)