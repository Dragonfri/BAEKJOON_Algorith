A = 300
B = 60
C = 10

time = int(input())

if time % C != 0:
    print(-1)
else:
    a = b = c = 0

    a = int(time / A)
    b = int((time % A) / B)
    c = int(((time % A) % B) / C)

    print(a, b, c)