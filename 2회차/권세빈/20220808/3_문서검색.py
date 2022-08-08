n = input()
m = input()
cnt = 0

# n에서 m과 같은 문자열은 모두 '*'로 바꾸기
r = n.replace(m,'*')

# 만약 i가 *이라면 카운트 + 1
for i in r:
    if i == '*':
        cnt += 1
print(cnt)
