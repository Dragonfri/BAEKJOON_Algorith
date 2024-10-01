test = int(input())

for i in range(test):
    a, b = map(int, input().split())
    # a가 큰값으로 설정
    if a < b:
        tmp = a
        a = b
        b = tmp
    # a나 b가 1이면 그냥 바로 출력
    if a == 1 or b == 1:
        print(a)
    #b가 a의 약수면 그냥 a를 출력
    elif a % b == 0:
        print(a)
    # 그 외의 경우는 공약수로 나눠가면서 계산 시작
    else:
        result = 1
        x = 2
        while b >= x * 2:
            if a % x == 0 and b % x == 0:
                result *= x
                a /= x
                b /= x
            else:
                if x == 2:
                    x += 1
                else:
                    x += 2

        result = result * a * b
        print(int(result))

