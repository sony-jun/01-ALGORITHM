#단어공부
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.




alp=input().upper()

chars={}

for char in alp:
    if char not in chars:
        chars[char]= 1
    else :
        chars[char]+= 1

reselt =max(chars,key=chars.get)
char_h1= chars.pop(max(chars,key=chars.get))

if len(chars) >=1:
        char_h2= chars.pop(max(chars,key=chars.get))#한가지 알파엣으로하면 딕셔너리가 비어서 오류남
        if char_h1 == char_h2 : # 비교할값이 
                 print('?')
        else:
            print(reselt)
else:
    print(reselt)

# if char_h1 == char_h2 : # 비교할값이 
#     print('?')
# else:
#     print(reselt)