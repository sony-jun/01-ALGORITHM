# https://www.acmicpc.net/problem/1357

x, y = input().split()      # 입력값 문자열로 받기
x = int(x[::-1])            # 슬라이스로 역순 후 정수로 변환
y = int(y[::-1])
print(int(str(x+y)[::-1]))  
# x+y를 한 후, 문자열로 바꿔서 슬라이스 역순하고, 다시 정수로 변환