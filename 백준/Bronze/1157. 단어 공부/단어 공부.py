c = input()

# 한글자면 그냥 소문자인지 체크하고 대문자로 바꿔서 출력
if len(c) == 1:
    if 'a' <= c <= 'z':
        c = chr(ord(c) - 32)
    print(c)
else:
    # 한글자 이상이면 소문자 대문자로 치환해주고
    # dictionary 타입에 key 값은 입력받은 대문자, value는 등장 횟수
    dict = {}
    sorted_dic = {}
    for i in c:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    
    # value 기준으로 정렬
    # 만약 정렬된 배열의 길이가 1이면 (ex. aaaaa 같이 한가지 글자만 반복되는 형태라면) 바로 출력)
    # 그 외의 경우에는 가장 높은 숫자가 2개 이상 존재하는지 확인
    # 2개 이상 존재하는 경우 '?' 출력, 아니면 index 0 출력(정렬 되어있으니까)
    sorted_dic = sorted(dict, key=lambda x: dict[x], reverse=True)
    if len(sorted_dic) == 1:
        print(sorted_dic[0])
    else:
        if dict[sorted_dic[0]] == dict[sorted_dic[1]]:
            print('?')
        else:
            print(sorted_dic[0])