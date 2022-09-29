import sys

a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result = str(result)

print(result.count('0'))
print(result.count('1'))
print(result.count('2'))
print(result.count('3'))
print(result.count('4'))
print(result.count('5'))
print(result.count('6'))
print(result.count('7'))
print(result.count('8'))
print(result.count('9'))

sys.stdin = open("0_숫자의개수.txt")

#개선.ver
a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c)) #a*b*c의 값을 문자열로 변환한 리스트를 result에 넣어준다. 

for i in range(10): #0-9까지 i에 넣어준다. 
    print(result.count(str(i)))