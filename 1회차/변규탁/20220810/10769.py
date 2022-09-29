N = input()

happy = ":-)"
sad = ":-("

if N.count(happy) == 0 and N.count(sad) == 0:
    print("none")

else:
    if N.count(happy) == N.count(sad):
        print("unsure")
    elif N.count(happy) > N.count(sad):
        print("happy")
    elif N.count(happy) < N.count(sad):
        print("sad")
