n = int(input())
if n == 1:
    pass
else:
    x = 2
    while n >= x * 2:
        if n % x == 0:
            print(x)
            n = n / x
            x = 2
        else:
            if x == 2:
                x += 1
            else:
                x += 2
    print(int(n))

