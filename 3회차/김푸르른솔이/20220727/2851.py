mushroom_list = []
result = 0
mario = 0
for i in range(10): #10번 반복해서 점수 입력
    mushroom_list.append(int(input()))

for mushroom in mushroom_list:
    mario += mushroom
    if abs(mario-100) <= abs(result-100):
        result = mario

print(result)