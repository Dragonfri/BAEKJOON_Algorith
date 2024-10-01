lst = []
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    lst.append(score)
print(int(sum(lst)/5))