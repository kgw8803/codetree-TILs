def print_hellow(n):
    if n == 0: 
        return
    print_hellow(n-1)
    print("HelloWorld")


n  = int(input())

print_hellow(n)