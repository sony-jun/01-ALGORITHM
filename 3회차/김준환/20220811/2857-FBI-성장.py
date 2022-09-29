lst = []
cnt = 0
for _ in range(5):
    lst.append(input())
for i in range(len(lst)):
    if 'FBI' in lst[i]:
        cnt += 1
        print(i+1)
if cnt == 0:
    print('HE GOT AWAY!')