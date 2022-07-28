sent = input().upper()
count_a = {}
# 딕셔너리 키에 알파벳을 값에 숫자를 넣었다
for i in sent:
    if i not in count_a:
        count_a[i] = 1
    else:
        count_a[i] += 1
# 딕셔너리의 가장 큰 값과 동일한 값이 있는지 찾아서 있다면 ?, 없다면 출력
count = 0
max_key= max(count_a, key = count_a.get)
for value in count_a.items():
    value = value[1]
    if int(count_a[max_key]) == value:
        count += 1
if count >= 2:
    print('?')
else:
    print(max(count_a, key = count_a.get))
