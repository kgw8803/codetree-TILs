N,  K = map(int, input().split())
arr = []

def choose(curr_num):
    if curr_num == N+1:
        print(*arr)
        return


    for i in range(1,K+1):

        arr.append(i)
        choose(curr_num + 1)
        arr.pop()


    

    return

choose(1)