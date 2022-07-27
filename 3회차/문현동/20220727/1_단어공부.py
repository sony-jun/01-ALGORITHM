import sys
sys.stdin = open("1_단어공부.txt", 'r')

input_str = input().upper() # baaa >>> BAAA

frequency = {} # 빈도수 키와 값 담을 딕셔너리

for i in input_str: # B A A A
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
# 딕셔너리에 알파벳당 출현 횟수를 키와 값의 형태로 저장

if list(frequency.values()).count(max(frequency.values())) >= 2:
    # frequency.values() 하면 알파벳 출현 횟수들이 나오는데 그걸 리스트로 만듦
    # 리스트로 만든 출현 횟수 중에,
    # max(frequency.values()) 가 몇 개 있는지 세는 조건문. max(frequency.values()) 는 임의의 최대 숫자이고 그것을 count 해서 리스트 안에 그 개수가 두 개 이상이면 print('?')
    # 즉, frequency의 최댓값을 값으로 가지는 키의 개수가 두 개 이상일 때 실행되는 조건문
    print('?')
else: # 한 개만 있으면 최대값의 키를 출력해줌
    for j in frequency:
        if frequency[j] == max(frequency.values()):
            print(j)