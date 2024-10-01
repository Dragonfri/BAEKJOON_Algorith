import math

x = int(input())
est_n = round(math.sqrt(x*2))
#print(est_n)
while True:
    if est_n * (est_n + 1) > x * 2:
        est_n -= 1
    else:
        break

print(int(est_n))