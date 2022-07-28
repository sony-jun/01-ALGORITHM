# 두 입력을 거꾸로 받아서 계산 후 다시 뒤집기
# 문자열로 두 입력 받는다, [:-1]사용
# 정수형 변환 후 계산
# 결과다시 문자열 출력

x, y = input().split()
s = int(x[::-1].lstrip('0')) + int(y[::-1].lstrip('0'))
print(str(s)[::-1].lstrip('0'))