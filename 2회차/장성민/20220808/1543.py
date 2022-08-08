doc = input()
word = input()
result = 0

while True:
    idx = doc.find(word)
    if idx == -1:
        break

    result += 1
    doc = doc[idx + len(word):]

print(result)