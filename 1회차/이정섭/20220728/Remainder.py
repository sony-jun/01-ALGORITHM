rem = []
for i in range(10):
    n = int(input())
    rem.append(n % 42)
rem = set(rem)
print(len(rem))

# Divide input by 42 
# use set() to get rid of duplicate numbers