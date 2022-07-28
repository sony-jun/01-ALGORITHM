# 다이얼 전화기 딕셔너리로 생성
dial = {
    '2' : ['A', 'B', 'C'],
    '3' : ['D', 'E', 'F'],
    '4' : ['G', 'H', 'I'],
    '5' : ['J', 'K', 'L'],
    '6' : ['M', 'N', 'O'],
    '7' : ['P', 'Q', 'R', 'S'],
    '8' : ['T', 'U', 'V'],
    '9' : ['W', 'X', 'Y', 'Z']
}

word = input()
sum = 0

# input의 word를 순회
for i in range(len(word)):
    # 키, 값 순회
    for k, v in dial.items():
        # 만약 word 글자가 값 리스트 안에 있다면
        if word[i] in v:
            # 키를 정수형으로 바꾼 후 빈 다이얼 때문에 1 더하고 sum에 더하기
            sum += int(k) + 1
print(sum)