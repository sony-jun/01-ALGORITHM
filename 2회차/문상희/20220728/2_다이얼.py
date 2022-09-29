alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time =  [3, 4, 5, 6, 7, 8, 9, 10]
# 각 알파벳들이 위치한 번호까지 돌리면 몇 초가 필요한지 자릿수에 맞게 바인딩한 리스트를 각각 생성해준다

count = 0
word = input()

for i in word:
    for j in range(8):
        if i in alpha[j]:
            count += time[j]
# 입력된 문자의 낱말이 alpha에 자릿수를 time에 위치한 값을 찾으면 걸리는 시간 찾을 수 있고
# 이 값을 0부터 시작해 계속 더해나가면 값을 구할 수 있다.
print(count)