while True:
    sentence = input()
    moem = ['a','e','i','o','u']
    cnt = 0
    for i in sentence:
        if i.lower() in moem:
            cnt+=1
    if sentence == '#':
        break
    else:
        print(cnt)