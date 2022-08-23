import sys
sys.stdin = open("02_단어공부_1157.txt", "r")


word = input().lower() # 대소문자 구분하지 않으므로 소문자로 # Mississipi
word_li = list(set(word)) # 중복 제거하여, "count할 문자만" # ["m", "p", "s", "i"]

cnt = []
for i in word_li:
    cnt.append(word.count(i)) # cnt = [1, 1, 4, 4] 가장 많은 알파벳의 count 횟수 기록

if cnt.count(max(cnt)) >= 2: # max(cnt) = 4
    print("?")
else:
    # ["m", "p", "s", "i"] # word_li
    # [ 1 ,  1 ,  4 ,  4 ] # cnt
    # [ 0 ,  1 ,  2 ,  3 ] # 각 리스트의 index
    print(word_li[cnt.index(max(cnt))].upper())

