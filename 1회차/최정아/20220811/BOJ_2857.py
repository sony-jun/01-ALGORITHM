li = []
for i in range(1, 6): # 인덱스 순회
    w = input()
    if "FBI" in w: # FBI 단어가 w에 있으면
        li.append(i) # li에 추가
if li:
    print(*li)
else:
    print("HE GOT AWAY!")