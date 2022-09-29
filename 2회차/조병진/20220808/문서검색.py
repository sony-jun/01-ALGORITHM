# 문서 검색 🐳
# 문제 : 문서에서 단어가 중복없이 총 몇 번 등장하는지 구하기

paper = input().strip()
word = input().strip()

answer = paper.count(word)

print(answer)
