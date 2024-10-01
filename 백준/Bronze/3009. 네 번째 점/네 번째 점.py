lst_x = []
lst_y = []
for i in range(3):
    a, b = map(int, input().split())
    lst_x.append(a)
    lst_y.append(b)

lst_x.sort()
lst_y.sort()

if lst_x[0] == lst_x[1]:
    x = lst_x[2]
else:
    x = lst_x[0]

if lst_y[0] == lst_y[1]:
    y = lst_y[2]
else:
    y = lst_y[0]

print(x, y)