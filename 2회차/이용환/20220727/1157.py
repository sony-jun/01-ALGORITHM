text_ = input()
result = []
for i in text_:
    if ord(i) > 96:
        c = chr(ord(i)-32)
        result.append(c)
    else:
        result.append(i)
cnt = {}
for j in result:
    if j in cnt:
        cnt[j] += 1
    else:
        cnt[j] = 1
print('?') if len([k for k,v in cnt.items() if max(cnt.values()) == v]) > 1 else print(max(cnt, key=cnt.get))
