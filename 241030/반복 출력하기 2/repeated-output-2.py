def print_hellow(n):
    if n == 0: 
        return
    print_hellow(n-1)
    print("HelloWorld")


print_hellow(4)