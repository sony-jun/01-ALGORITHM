word = input()
keyword = input()
n = 0
cnt = 0
while n <= len(word) - len(keyword):
    if word[n:n+len(keyword):] == keyword:
        cnt += 1
        n += len(keyword)
    else:
        n += 1
print(cnt)