import sys
sys.stdin = open('1543.txt')

word = input() ## aaaaaaa
word_ser = input() ## aa

#print(word, word_ser)

print(word.split(word_ser))

word_rem = ''.join(word.split(word_ser))
print(word_rem)
#print(len(word_rem))

word_num = (len(word) - len(word_rem)) / len(word_ser)
print(len(word))
print(len(word_rem))
print(len(word_ser))

print(int(word_num))


############## 최준혁님 ##########################

doc = input()
search = input()
cnt = 0
n = 0
while n  <= len(doc) - len(search): # 문서 길이에서 검색길이를 뺀 값이 n보다 크거나 같을때까지
    if doc[n:n+len(search)] == search: # doc의 n부터 n+검색길이 값이 검색과 같다면?
        cnt += 1 # 카운트 증가
        n += len(search) # 검색길이만큼 인덱스를 증가 
    else: # 찾을수 없으면
        n += 1 # 인덱스를 1씩 올려주며 탐색

print(cnt)