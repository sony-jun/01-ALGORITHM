#https://www.acmicpc.net/problem/2941

#문자열 앞뒤로 2개 씩비교...char[i: i+2]... 가능하지만 번거롭다
#특수한 경우인 예시 미리 리스트에 저장해두고 replace로 한 자리로 변경하자

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croa:
    word = word.replace(i, "C")
print(len(word))

