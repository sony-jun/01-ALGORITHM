# KMP는 왜 KMP일까?

word = input()
result = ''
for a in word:
    if (ord(a) >= 65) and (ord(a) <= 90):
        result += a
print(result)