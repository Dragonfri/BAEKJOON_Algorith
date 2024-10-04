a, b = input().split()

# a가 무조건 길게 조정. 길이가 같으면 상관없음
if len(a) < len(b):
    tmp = a
    a = b
    b = tmp

b = b.zfill(len(a))

a = list(a)
b = list(b)
a.reverse()
b.reverse()

result = []
upper = 0
for i in range(len(a)):
    if (int(a[i]) + int(b[i]) + upper) > 9:
        result.append((int(a[i]) + int(b[i]) + upper) % 10)
        upper = 1
    else:
        result.append(int(a[i]) + int(b[i]) + upper)
        upper = 0
    if i == len(a) - 1 and upper == 1:
        result.append(1)

result.reverse()
result = list(map(str, result))

print(''.join(result))