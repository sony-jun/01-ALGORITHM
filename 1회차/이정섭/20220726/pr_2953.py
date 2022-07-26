

score = [sum(list(map(int,input().split()))) for i in range(5)]
print(score.index(max(score))+1,max(score))

# use index method to point out which one is has the max score
# use index +1 since Python uses zero-based indexing


# Alt 1

# score = []

# for i in range(5) :
#   score.append(sum(map(int, input().split())))

# print(score.index(max(score))+1, max(score))