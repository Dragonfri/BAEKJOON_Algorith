from sys import stdin

dic = {}

test = int(input())

for i in range(test):
    arr = list(stdin.readline().split())
    if arr[0] == "all" or arr[0] == "empty":
        op = arr[0]
        if op == "all":
            dic = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1,
               17: 1, 18: 1, 19: 1, 20: 1}
            continue
        elif op == "empty":
            dic = {}
            continue

    op, x = arr[0], arr[1]
    x = int(x)

    if op == "add":
        dic[x] = 1
    elif op == "remove":
        if dic.get(x):
            del (dic[x])
    elif op == "check":
        if dic.get(x):
            print(1)
        else:
            print(0)
    elif op == "toggle":
        if dic.get(x):
            del (dic[x])
        else:
            dic[x] = 1

