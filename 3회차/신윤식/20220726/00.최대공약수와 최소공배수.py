N_1, N_2 = map(int,input().split())

N = max(N_1, N_2)
lst = []

for i in range(1, N+1):
    if N_1 % i == 0 and N_2 % i == 0:
        lst.append(i)
    
Greatest = lst[-1]
print(Greatest)
print(Greatest * (N_1//Greatest) * (N_2//Greatest))