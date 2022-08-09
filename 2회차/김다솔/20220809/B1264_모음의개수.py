# https://www.acmicpc.net/problem/1264
import sys
sys.stdin = open('B1264.txt')

vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    sentence = input().lower()
    cnt = 0
    # print(sentence)
    if sentence == '#':
        break
    
    else:
        for i in range(len(sentence)):
            if sentence[i] in vowels:
                cnt += 1
        print(cnt)
    
        