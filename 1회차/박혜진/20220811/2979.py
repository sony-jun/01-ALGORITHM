a, b, c = map(int, input().split())

parking = []
costs = {}

for _ in range(3) :
    car_in, car_out = input().split()

    for i in range(int(car_in), int(car_out)) :
        parking.append(i)

    for j in set(parking) :
        costs[j] = parking.count(j)
    
    parking_cost = 0
    for p in costs.values() :
        if p == 1 :
            parking_cost += p * a
        
        elif p == 2 :
            parking_cost += p * b

        else :
            parking_cost += p * c

print(parking_cost)