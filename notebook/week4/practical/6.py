def multiply(a, b=None):
    if b is None:
        return a * a
    return a * b

print(multiply(5, 4))   # 20
print(multiply(7))      # 49
print(multiply(3, 10))  # 30
