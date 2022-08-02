def merge(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low = merge(arr[:mid])
    high = merge(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merged_arr.append(low[l])
            l += 1
        else:
            merged_arr.append(high[h])
            h += 1
    merged_arr += low[l:]
    merged_arr += high[h:]
    return merged_arr