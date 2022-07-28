# 나머지 

number_list = []
for _ in range(10):
    number_list.append((int(input())) % 42) # 미리 42로 나누어 리스트에 할당

result_list = list(set(number_list))    # 서로 다른 수의 개수만 구하면 되기 때문에  
count = 0                               # 중복 제거 후 개수만 구한다.
for _ in result_list:
    count += 1
print(count)