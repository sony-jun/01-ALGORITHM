n = int(input())
for geum in range(n,-1,-1):
    g_len = len(str(geum))
    cnt = 0
    for s in str(geum):
        if s == '4' or s == '7':
            cnt+=1
    if cnt == g_len:
        print(geum)
        break