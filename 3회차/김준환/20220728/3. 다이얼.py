# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 순서로 인덱스 번호가 숫자
# [1:4],[4:7],[7:10],[10:13][13:17][17:21][21:24][24:28
# [2,3,    9] 까지 각 숫자에 위의 범위로 되도록 리스트 제작
# 알파벳을 문자열 알파벳에서 찾아서 인덱스가 어떤 숫자 범위에 있는지 확인후 숫자 출력

num = input()
cnt = 0
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for text in num:
    if alpha.index(text) < 3:
        cnt += 3
    elif alpha.index(text) < 6:
        cnt += 4
    elif alpha.index(text) < 9:
        cnt += 5
    elif alpha.index(text) < 12:
        cnt += 6
    elif alpha.index(text) < 15:
        cnt += 7
    elif alpha.index(text) < 19:
        cnt += 8
    elif alpha.index(text) < 22:
        cnt += 9
    elif alpha.index(text) < 26:
        cnt += 10
print(cnt)