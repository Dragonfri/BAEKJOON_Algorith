test = int(input())

for i in range(test):
    y_score = k_score = 0
    for i in range(9):
        y, k = map(int, input().split())
        y_score += y
        k_score += k

    if y_score == k_score:
        print("Draw")
    elif y_score > k_score:
        print("Yonsei")
    else:
        print("Korea")