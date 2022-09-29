import sys
sys.stdin = open("93_문서 검색.txt", "r")

para = input()
text = input()

start = 0
cnt = 0
while True:
    if text in para:
        # "문서para에서 찾을 단어text의 index + text의 길이"부터 다시 탐색하기 위해 값 변경
        para = para[para.index(text) + len(text): ]
        cnt += 1
    else:
        break

print(cnt)