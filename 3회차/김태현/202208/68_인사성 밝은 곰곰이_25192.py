import sys
sys.stdin = open("68_인사성 밝은 곰곰이_25192.txt", "r")

T = int(input())

result = {}
cnt = 0

for i in range(T):

    text = input()

    if text == "ENTER":
        result = {}

    else:
        if result.get(text, 0):
            result[text] += 1
        else:
            cnt += 1
            result[text] = 1

print(cnt)