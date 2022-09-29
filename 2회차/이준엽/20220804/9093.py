t = int(input())
for i in range(t):
    sentence = list(input().split())
    for i in range(len(sentence)):
        sentence[i] = sentence[i][::-1]
    print(*sentence)