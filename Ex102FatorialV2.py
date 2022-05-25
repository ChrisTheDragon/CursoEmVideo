def fatorial(n=1, show=False):
    f = 1
    for i in range(n, 0, -1):
        if show == True:
            print(i, end='')
            if i>1:
                print(f' X ', end='')
            else:
                print(f' = ', end='')
        f *= i
    return f



print(fatorial(5))
print(fatorial(4, True))
print(fatorial(10))
print(fatorial(9, True))
