import sys
sys.stdin = open('행복한지슬픈지_input.txt')

sentence = input()

happy = ':-)'
sad = ':-('
h_count = 0
s_count = 0

h_count = sentence.count(happy)
s_count = sentence.count(sad)

if h_count > s_count:
    print('happy')
elif h_count < s_count:
    print('sad')
elif h_count > 0 and s_count > 0 and h_count == s_count:
    print('unsure')
else:
    print('none')