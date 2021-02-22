def binr_search(array, value):
    left = 0
    right = len(array) - 1
    pos = len(array) // 2 - 1

    while array[pos] != value and left <= right:
        if array[pos] > value:
            right = array[pos] - 1
        else:
            left = array[pos] + 1
        pos = (left + right) // 2

        return -1 if left > right else pos


