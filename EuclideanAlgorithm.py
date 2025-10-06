def EuclidianAlgorithm(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


print(EuclidianAlgorithm(7975, 2585))
