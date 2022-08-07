import heapq

numbers = [5, 3, 2, 4, 1]

heapq.heapify(numbers)
print(numbers)
heapq.heappop(numbers)
print(numbers)
heapq.heappush(numbers ,0)


print(numbers)

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,0,1,2]

        ]  
total = sum(map(sum,matrix)) 
print(total)
# n * m
n = len(matrix)
m = len(matrix[0])

total = 0
for i in range(n): 
    for j in range(m):
        total += matrix[i][j]
print(total)

for row in matrix:
    total += sum(row)
print(total)


def matrix_sum(matrix):
    return (sum(map(sum,matrix)))