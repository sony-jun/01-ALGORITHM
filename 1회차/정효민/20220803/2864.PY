min_result = 0
max_result = 0
a , b = input().split()

min_result = int(a.replace('6' , '5')) + int(b.replace('6' , '5'))
max_result = int(a.replace('5' , '6')) + int(b.replace('5' , '6'))
print(min_result , max_result)

    