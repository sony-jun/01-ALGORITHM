N = int(input())
 
for i in range(N):
    M = sum(map(int, str(i)))
    result = i + M
    if result == N:
        print(i)
        break
else:
    print(0)

# Change i into string so i can added one by one and turn back to int

# Q1
# why if you input 198 at 'N', the output is 0.
# Because if N is 184 then, M should  197
# If N is 185 then, M should be 199



# Wrong

# N = int(input())
 
# for i in range(N):
#     M = sum(map(int, (i)))
#     result = i + M
#     if result == N:
#         print(i)
#         break
# else:
#     print(0)

# Traceback (most recent call last):
#  line in <module>  M = sum(map(int, (i)))
# TypeError: 'int' object is not iterable