num = int(input())
vote = list(input())
vote.sort()
if num == 1:
    print(vote[0])
else:
    if num % 2 == 0:
        num = int(num/2)
        if vote[num] == vote[num-1]:
            print(vote[num])
        else:
            print("Tie")
    else:
        print(vote[int(num/2)])