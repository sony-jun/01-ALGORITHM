import sys
sys.stdin = open('상금헌터_input.txt')

money1 = [[500,1],[300, 2],[200, 3],[50, 4],[30, 5],[10, 6]]
money2 = [[512,1],[256, 2],[128, 4],[64, 8],[32, 16]]

T = int(input())

rank = [input().split() for _ in range(T)]

#print(rank) #[['8', '4'], ['13', '19'], ['8', '10'], ['18', '18'], ['8', '25'], ['13', '16']]

if rank[0][0] 