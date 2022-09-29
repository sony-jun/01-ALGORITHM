msg = input()

h = msg.count(":-)")
s = msg.count(":-(")

if not h and not s:
    print("none")
elif h == s:
    print("unsure")
elif h > s:
    print("happy")
else:
    print("sad")