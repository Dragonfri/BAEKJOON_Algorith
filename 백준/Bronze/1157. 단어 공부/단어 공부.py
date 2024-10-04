c = input()

if len(c) == 1:
    if 'a' <= c <= 'z':
        c = chr(ord(c) - 32)
    print(c)
else:
    dict = {}
    sorted_dic = {}
    for i in c:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    sorted_dic = sorted(dict, key=lambda x: dict[x], reverse=True)
    if len(sorted_dic) == 1:
        print(sorted_dic[0])
    else:
        if dict[sorted_dic[0]] == dict[sorted_dic[1]]:
            print('?')
        else:
            print(sorted_dic[0])