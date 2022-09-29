import sys
sys.stdin = open("02_단어공부_1157.txt", "r")


word = input().lower() # 대소문자 구분이 없다고 했으므로 lower 메소드로 모두 소문자로 바꿔준다.
alphabet = list(set(word))
count_list = []
for i in range(len(alphabet)):
    if word.count(alphabet[i]) > word.count(alphabet[i-1]):
        result = alphabet[i]
    elif word.count(alphabet[i]) < word.count(alphabet[i-1]):
        result = alphabet[i-1]
    else:
        result = "?"
print(result)