n, m = input().split()

s = 'S' * int(n)
a = 'A' * int(m)

new_string = ""
for s1, a1 in zip(s, a):
    new_string += s1 + a1
print(new_string.count("SASA"))
# 다른 방법
# result = ''.join(map(''.join, zip(s, a)))
# print(result.count("SASA"))