from turtle import right


def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    # 엇갈리기 전까지 반복
    while(left <= right):
        # pivot 보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
            print(left, end)
        
        while