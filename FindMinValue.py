def find_min_value(values):
    minValue = values[0]

    for value in values:
        if value < minValue:
            minValue = value

    return minValue


values = [99, 150, 41, 2022, 104, 23, 134, 221]
result = find_min_value(values)
print(result)
