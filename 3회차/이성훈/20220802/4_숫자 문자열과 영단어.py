# https://www.acmicpc.net/problem/2609
import sys

sys.stdin = open("4_숫자 문자열과 영단어.txt")


def solution(s):
    
    
    while True:
        if 'one' in s:
            s = s.replace('one','1')
        elif 'two' in s:
            s = s.replace('two', '2')
        elif 'three' in s:
            s = s.replace('three', '3')
        elif 'four' in s:
            s = s.replace('four', '4')
        elif 'five' in s:
            s = s.replace('five', '5')
        elif 'six' in s:
            s = s.replace('six', '6')
        elif 'seven' in s:
            s = s.replace('seven', '7')
        elif 'eight' in s:
            s = s.replace('eight', '8')
        elif 'nine' in s:
            s = s.replace('nine', '9')
        elif 'zero' in s:
            s = s.replace('zero', '0')
        else:
            break
    p = int(s)
    
    answer = p
    return answer

print(solution( "one4seveneight"))



# test

# s = "2three45sixseven"

# while True:
#     if 'one' in s:
#         s = s.replace('one','1')
#     elif 'two' in s:
#         s = s.replace('two', '2')
#     elif 'three' in s:
#         s = s.replace('three', '3')
#     elif 'four' in s:
#         s = s.replace('four', '4')
#     elif 'five' in s:
#         s = s.replace('five', '5')
#     elif 'six' in s:
#         s = s.replace('six', '6')
#     elif 'seven' in s:
#         s = s.replace('seven', '7')
#     elif 'eight' in s:
#         s = s.replace('eight', '8')
#     elif 'nine' in s:
#         s = s.replace('nine', '9')
#     elif 'zero' in s:
#         s = s.replace('zero', '0')
#     else:
#         break
# p = int(s)
# print(p,type(p))