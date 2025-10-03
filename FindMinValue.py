values = [99, 150, 41, 2022, 104, 23, 134, 221]
minValue = 99999999999

for i in range(len(values)):
    if values[i] < minValue:
        minValue = values[i]

print(minValue)
