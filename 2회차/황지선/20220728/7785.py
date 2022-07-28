# 7785번 회사에 있는 사람

# 수를 받고
# 이름이랑 enter / leave 상태받고
# for문 이용해서 dictionary에 이름과 상태 넣기
# 차피 같은 이름인데 퇴근한 경우는 밸류값이 바뀌니까
# 그대로 읽어와서 for문에 enter 아닌 경우만 출력하게 하면 될듯?

n = int(input())
dict = {} # key : name, value : status_

for i in range(n):
    name, status_ = input().split()
    dict[name] = status_

# dict = {'Baha': 'leave', 'Askar': 'enter', 'Artem': 'enter'}

for j in dict:
    if dict[j] == 'enter' :
        print(j)

# Askar
# Artem