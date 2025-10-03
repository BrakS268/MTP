values = [99, 150, 41, 2022, 104, 23, 134, 221]
minValue = values[0]

for value in values:
    if value < minValue:
        minValue = value

print(minValue)
