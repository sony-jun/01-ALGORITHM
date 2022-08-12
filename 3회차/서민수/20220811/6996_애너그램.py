# 두 단어 A와 B가 주어졌을 때, A에 속하는 알파벳의 순서를 바꾸어서 B를 만들 수 있다면, 
# A와 B를 애너그램이라고 한다.

# 두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수(<100)가 주어진다.
#  각 테스트 케이스는 한 줄로 이루어져 있고, 
# 길이가 100을 넘지 않는 단어가 공백으로 구분되어서 주어진다. 
# 단어는 알파벳 소문자로만 이루어져 있다.

import sys


sys.stdin = open("input.txt")

# 3번반복
t = int(input())
for _ in range(t):
    # a,b 문자열 인풋
    a,b = map(str, input().split())
    # a와 b를 리스트 후 정렬
    anagram = sorted(list(a))
    noanagram = sorted(list(b))
    #print(anagram,noanagram)
    # anaramg 과 noana가 같다면
    if anagram == noanagram:
        # f스트링
        print("{} & {} are anagrams.".format(a,b))
        # print(" %s & %s are anagrams." %(anagram,noanagram))
    else: 
        print("{} & {} are NOT anagrams.".format(a,b))
        # print("{} & {} are NOT anagrams.".format(anagram,noanagram))
