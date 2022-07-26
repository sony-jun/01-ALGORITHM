A, B = map(int, input().split())

min_value = min(A, B)
GCF = 0
for i in range(1, min_value+1):
    if A % i == 0 and B % i == 0:
        GCF = i
        
print(GCF)

LCM = int(GCF * (A/GCF) * (B/GCF))

print(LCM)

