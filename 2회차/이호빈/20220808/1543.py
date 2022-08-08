#두 개의 입력값을 받아준다.
paper = input()
word = input()
#검색한 수가 몇 개 있는지 세주는 변수
result = 0
#입력값이 있을때까지
while paper:
    #문서에 인덱스를 접근해 검색해야하는 문자의 길이만큼 범위를 지정해서 맞으면 1을 더해주고 
    if paper[:len(word)] == word:
        result += 1
        #중복되면 안 되니까 다음 검색하려고하는 범위로 넘어간다.
        paper = paper[len(word):]
    #만약에 일치하는 값이 없으면 앞글자 한 글자씩 삭제 해준다.
    else:
        paper = paper[1:]

print(result)
