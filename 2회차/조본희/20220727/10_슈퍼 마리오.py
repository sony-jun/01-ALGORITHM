mushroom = []
for i in range(10):
    mushroom.append(int(input()))

temp = 0
sum1 = 0
for i in mushroom:
    temp += i
    if temp >= 100:
        if abs(temp - 100) <= abs(sum1 - 100):
            print(temp)
            break
        else:
            print(sum1)
            break
    sum1 += i

# 10개를 다 더해도 100에 미치지 않을 경우를 위한 조건문
if temp < 100:
    print(temp)