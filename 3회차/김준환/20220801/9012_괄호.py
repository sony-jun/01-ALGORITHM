# 괄호 '('는 1  ')' 는 -1 로 받으면 합이 -1이 되는 순간이 오면 괄호 법칙은 깨진다.

n = int(input())
for _ in range(n):
    text = input()
    answer = 'YES'
    cnt = 0
    for i in text:
        if i == '(':
            cnt += 1
            # print(cnt)
        else:
            cnt -= 1
            # print(cnt)
        if cnt == -1:
            answer = 'NO'
            break
    if cnt != 0:
        answer = 'NO'
    print(answer)