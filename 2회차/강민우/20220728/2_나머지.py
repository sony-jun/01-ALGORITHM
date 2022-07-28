rest = []

for a in range(10) :
    N = int(input())
    rest.append(N % 42)
    
print(len(set(rest)))
