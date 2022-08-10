import sys
input = sys.stdin.readline

sen= str(input()) #문장 받기

happyy = sen.count(':-)') #count함수로 이모티콘의 개수 세기
sadd = sen.count(':-(')

if sadd < happyy:
    print('happy')
elif sadd > happyy:
    print('sad')
elif happyy == 0 and sadd == 0:
    print('none')
else :
    print('unsure')