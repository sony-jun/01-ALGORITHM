# https://www.acmicpc.net/problem/2851


# 열개의 숫자를 받아서
# 처음부터 쭈르르륵 더한다 언제까지? 100을 넘을때까지
# 100이 넘으면 출력을 하는데
# 100 을뺸 절대값이 가까운거로
# 근데 두개가 같다? 그럼 둘중 큰숫자로

i = 0
hap1 = 0
hap2 = 0

while i < 10 :
    i += 1
    T = int(input())
    if hap1 < 100:
        hap2 = hap1
        hap1 += T
    else:
        continue

if abs(hap1 - 100) > abs(100 - hap2):
    print(hap2)
else:
    print(hap1)
