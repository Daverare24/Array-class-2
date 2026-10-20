
def arrayMean(arr, arr_size):
    total_sum = 0
    for i in range(0, arr_size):
        total_sum += arr[i]
    return float(total_sum / arr_size)


def arrayMedian(arr, arr_size):
    arr = sorted(arr)

    if arr_size % 2 != 0:
        return float(arr[arr_size // 2])

    return float((arr[arr_size // 2 - 1] + arr[arr_size // 2]) / 2)


arr = [1, 4, 5, 6, 2, 3, 7, 8, 9]
arr_size = len(arr)

print("Mean =", arrayMean(arr, arr_size))
print("Median =", arrayMedian(arr, arr_size))
