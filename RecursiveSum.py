def Recursive_Sum(num):
    if num == 1:
        return 1
    else:
        return num + Recursive_Sum(num - 1)


print(Recursive_Sum(5))
print(Recursive_Sum(10))
print(Recursive_Sum(1))
