def binary_array_to_number(arr):
    a = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            a += 2**(len(arr) - 1 - i)

    return a