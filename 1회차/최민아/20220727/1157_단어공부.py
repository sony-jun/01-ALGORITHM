import sys
sys.stdin = open("20220727/1157_단어공부.txt")

word_upper = input().upper()
alphabet = list(set(word_upper))

alphabet_cnt = [word_upper.count(i) for i in alphabet]

max_cnt = max(alphabet_cnt)

if alphabet_cnt.count(max_cnt) > 1:
    print('?')
else:
    max_alphabet = alphabet_cnt.index(max_cnt)
    print(alphabet[max_alphabet])