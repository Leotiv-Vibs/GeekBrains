def razm(big_array):
    array_minus = []
    array_plus = []
    for i in big_array:
        if i >= 0:
            array_plus.append(i)
        else:
            array_minus.append(i)
    return array_minus, array_plus
print(razm([1,2,3,4,5,-1,-2,-3,-4,-5]))