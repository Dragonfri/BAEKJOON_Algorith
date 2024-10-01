test = int(input())
for i in range(test):
    arr = input().split()
    num = int(arr[0])
    for j in arr[1]:
        print(j*num, end='')
    print()

