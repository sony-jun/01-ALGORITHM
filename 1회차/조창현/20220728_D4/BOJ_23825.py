#s, a = 4, 5

s, a = map(int, input().split())

s_divi = int(s / 2)
a_divi = int(a / 2)
#print(s_divi, a_divi)

if s_divi < a_divi:
    print(s_divi)
else:
    print(a_divi)