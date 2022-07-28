N , M = map(int , input().split())

sb = N / 2
ab = M / 2

result = [int(sb) , int(ab)]
print(min(result))



# block = {
#     'SB' : N ,
#     'AB' : M
    
# }

# while block['SB'] >= 2 and block['AB'] >= 2:
#     block['SB'] = block['SB'] - 2
#     block['AB']= block['AB'] - 2
#     result_sasa += 1
# print(result_sasa)