import sys
sys.stdin = open("9. 문서검색.txt", "r")

word = input() # 문서
search = input() # 검색할 단어
cnt = 0 # 단어 등장 수
i = 0 # 인덱스

while len(word) - i >= len(search): 
    # 문서의 길이에서 i(인덱스)를 뺸 값이 word 길이보다 크거나 같을때 반복 진행
    
    if word[i:i+len(search)] == search: 
        # word의 현재 i에서 i+검색단어의 길이만큼 더한 단어가 검색 단어와 같다면,
        cnt +=1 
        # cnt 1 증가
        i += len(search)
        # i를 검색 단어의 길이만큼 증가
    else:
        i += 1 # 같지 않으면 i에 +1
print(cnt)