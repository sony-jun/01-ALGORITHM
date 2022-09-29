# {key: 영단어, value: 숫자}
# if key in s:
#   replace(key, dic[key])

import sys
sys.stdin = open("65_숫자 문자열과 영단어.txt", "r")

dic = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

for i in range(4):
    s = input()

    for key in dic.keys():
        if key in s:
            s = s.replace(key, dic[key])

    print(int(s))