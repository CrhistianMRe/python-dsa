def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    first = 0
    second = 1

    for i in range(0, n - 1):
            temp = second
            second = first + second
            first = temp 


    return second
        
