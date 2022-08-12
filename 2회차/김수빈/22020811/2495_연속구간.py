for i in range(3):
    list_ = list(input())
    cnt = 1
    max = 1

    for j in range(7):
        if list_[j] == list_[j + 1]:
            cnt += 1
            if cnt > max:
                max = cnt
        else:
            cnt = 1

    print(max)