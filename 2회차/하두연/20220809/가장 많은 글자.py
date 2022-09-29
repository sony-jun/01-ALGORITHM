# 백준 1371

# 영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.

# 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

import sys

word = sys.stdin.read()
word = word.replace('\n','').replace(' ','')

dict ={}

for i in word:
    for j in i:
    