def fibonnaci(n):
    i = 0
    j = 1
    fib = 0
    while (fib <= n):
        print(i)
        fib = i
        i = j
        j = fib + i
