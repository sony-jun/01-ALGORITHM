import sys
sys.stdin = open('1371.txt')
import sys
word = sys.stdin.read().replace('\n','').replace(' ','')
word_list = [0] *26

for i in word:
    word_list[ord(i)-97] += 1

for j in range(len(word_list)):
    if word_list[j] == max(word_list):
        print(chr(97+j), end='')