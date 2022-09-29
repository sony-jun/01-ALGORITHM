a,b,c = map(int,input().split())
trucks = [list(map(int,input().split())) for i in range(3)]

max_time = max(list(max(trucks[i]) for i in range(3)))
parking = [0]*(max_time)

for truck in trucks:
    for i in range(truck[0],truck[-1]):
        parking[i]+=1

fees = 0

for i in parking:
    if i == 1:
        fees+=a*i
    elif i == 2:
        fees+=b*i
    elif i ==3:
        fees+=c*i
print(fees)