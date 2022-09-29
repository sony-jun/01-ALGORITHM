list_ = [int(input()) for _ in range(3)]

good = sum(list_)

if good == 180:
    if list_[0] == list_[1] == list_[2]:
        print('Equilateral')
    elif list_[0] == list_[1] or list_[0] == list_[2] or list_[1] == list_[2]:
        print('Isosceles')
    elif list_[0] != list_[1] != list_[2]:
        print('Scalene')
else:
    print('Error')