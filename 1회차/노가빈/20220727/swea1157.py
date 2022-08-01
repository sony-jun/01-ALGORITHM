char = list(input())
count = []
for i in char:
    if ord(i) >90 :
        count.append(chr(ord(i)-32))
    else:
        count.append(i)

num_count = {}
for num in count:
    num_count[num] = 0 # 특정 문자 딕셔너리에 추가
for num in count:
    num_count[num] = num_count[num] + 1 # 추가한 딕셔너리에서 갯수 더하기

maxChar=''
maxcount = 0
for key, value in num_count.items(): # 키와 값 모두 출력
    if maxChar != key and value > maxcount:
        maxChar=key
        maxcount=value
    elif maxChar != key and value == maxcount:
        maxChar = "?"
print(maxChar)