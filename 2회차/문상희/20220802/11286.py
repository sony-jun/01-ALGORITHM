import heapq
import sys
input = sys.stdin.readline

n = int(input())

numbers = []

for _ in range(n):
    i = int(input())
    numbers.append(i)

heap = []
num_cnt = dict()

for number in numbers:
    if number < 0:
        number *= -1
        if number in num_cnt:
            num_cnt[number] += 1
        else:
            num_cnt[number] = 1
        # 음수 입력시 절대값을 힙에 입력하고 넣은 음수의 개수를 세어줍니다.

    if number != 0:
        heapq.heappush(heap, number)
    else:
        if len(heap) == 0:
            print(0)
        else:
            if heap[0] in num_cnt:
                if num_cnt[heap[0]] > 0:
                    num_cnt[heap[0]] -= 1 
                    print((heapq.heappop(heap)) * - 1)
                    # 음수가 입력된 적 있는 절대값이 출력시 음수가 입력됬던 수만큼 
                    # 그 절대값에 대하여 -1을 곱하여 출력해주고 나머지를 출력하게 해줍니다.

                else:
                    print(heapq.heappop(heap))
            else:
                print(heapq.heappop(heap))