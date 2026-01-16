def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print(calcAve(1, 2, 3))
print(calcAve(10, 20))
print(calcAve(5, 10, 15, 20))
