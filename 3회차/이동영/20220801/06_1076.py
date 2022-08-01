dict1 = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}

dict2 ={
    'black' : 1,
    'brown' : 10,
    'red' : 100,
    'orange' : 1000,
    'yellow' : 10000,
    'green' : 100000,
    'blue' : 1000000,
    'violet' : 	10000000,
    'grey' : 100000000,
    'white' : 1000000000
}
list_ = []
for i in range(3):
    list_.append(input())

print(((dict1[list_[0]]*10) + (dict1[list_[1]])) * dict2[list_[2]])