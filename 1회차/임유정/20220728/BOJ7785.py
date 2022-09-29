# 회사에 있는 사람
N = int(input())
logs = dict()
for i in range(N):
    # 공백으로 나눠진 두개의 단어
    # print(input().split())
    key, value = input().split()
    logs[key] = value
    # logs["Baha"] = "enter"
    # logs["Askar"] = "enter"
    # logs["Baha"] = "leave"
    # logs["Artem"] = "enter"

# print(logs)

list_ = []
for key in logs :
    print(key)
    # value가 enter인 key를 찾아서 리스트에 저장
    if logs[key] == "enter":
            list_.append(key)

# print(list_)
list_.sort(reverse=True)
# 한 줄 씩 출력
for name in list_:
    print(name)
