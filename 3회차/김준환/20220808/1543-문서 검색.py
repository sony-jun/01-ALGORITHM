data = input()         # ababababa
search = input()       # aba

n = len(search)        # 3
cnt = 0
i = 0
while i < len(data)-n+1:       # 뒤에서 3번째 인덱스
    if data[i:i+n] == search:  
        cnt += 1
        i += n
    else:
        i += 1
print(cnt)
