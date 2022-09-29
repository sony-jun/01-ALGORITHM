for _ in range(3):
    line = input()
    ret = 0

    for i in range(10):
        for j in range(2, 9):
            if str(i) * j in line:
                if ret < j:
                    ret = j
            else:
                break

    print(ret) if ret else print(1)