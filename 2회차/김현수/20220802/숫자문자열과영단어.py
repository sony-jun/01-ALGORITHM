import sys
sys.stdin = open('숫자문자열과영단어.txt', 'r')

# one4seveneight	1478
# 23four5six7	234567
# 2three45sixseven	234567
# 123

str_ = input() #입력받는 변수
answer = str_ #입력받은 변수를 조작하기 위한 변수

number = {'zero':0,'one':1,'two':2,'three':3,
              'four':4,'five':5,'six':6,'seven':7,
              'eight':8,'nine':9}

for i in number.keys():
    if i in answer:
        answer = answer.replace(i, str(number[i]))
    
print(answer)