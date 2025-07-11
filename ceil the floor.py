def getFloorAndCeil(a, n, x):
    floor = -1
    ceil = -1

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == x:
            return [x, x]
        elif a[mid] < x:
            floor = a[mid]
            low = mid + 1
        else:
            ceil = a[mid]
            high = mid - 1

    return [floor, ceil]
