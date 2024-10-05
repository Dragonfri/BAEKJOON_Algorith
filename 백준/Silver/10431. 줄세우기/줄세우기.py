test = int(input())

for i in range(test):
    case = list(map(int, input().split()))

    num, arr = case[0], case[1:]
    count = 0

    tmp_arr = []
    for x in range(20):
        for y in range(x):
            if tmp_arr[y] > arr[x]:
                count += (x - y)
                break
        tmp_arr.append(arr[x])
        tmp_arr.sort()

    print(num, count)