s = int(input())

if s < 60:
    s = "F"
elif s < 70:
    s = "D"
elif s < 80:
    s = "C"
elif s < 90:
    s = "B"
else:
    s = "A"

print(s)