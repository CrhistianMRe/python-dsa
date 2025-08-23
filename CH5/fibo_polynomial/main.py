def fib(n):
    current = n
    grandparent = 0
    parent = 1
    for a in range(n-1):
        current = parent + grandparent
        grandparent = parent 
        parent = current 
    return current  

def main():
    print(fib(4))
main()





