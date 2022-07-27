# https://www.acmicpc.net/problem/2941

words = ['c=','c-','dz=','d-','lj','nj','s=','z=']

input_word = input()

for word in words:
    input_word = input_word.replace(word,'o')

print(len(input_word))