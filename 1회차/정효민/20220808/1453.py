
result = 0
pc_room_all = []
visit_number = int(input())
visit = list(map(int , input().split()))
for pc_room in range(1 , 101):
    pc_room_all.append(pc_room)
for number in visit:
    if number in pc_room_all:
        pc_room_all.remove(number)
    elif number not in pc_room_all:
        result = result + 1

print(result)
