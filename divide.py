# File: example.py

def divide(a, b):
    result = a/b
    return result

# Intentionally introducing division by zero issue
result = divide(10, 0)
print(result)
