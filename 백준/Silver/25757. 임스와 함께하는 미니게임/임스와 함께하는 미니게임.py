import sys

Y = 2
F = 3
O = 4

num, play = sys.stdin.readline().split()
num = int(num)
s = set()
for i in range(num):
    tmp = sys.stdin.readline()
    s.add(tmp)

if play == "Y":
    print(len(s))
elif play == "F":
    print(int(len(s) / (F - 1)))
else:
    print(int(len(s) / (O - 1)))
