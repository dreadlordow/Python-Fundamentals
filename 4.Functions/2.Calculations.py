def perform_operation(a, b, operation):
    if operation == 'add':
        return a + b
    if operation == 'subtract':
        return a - b
    if operation == 'divide':
        return a / b
    if operation == 'multiply':
        return a * b

operation = input()
a = int(input())
b = int(input())

print(int(perform_operation(a, b, operation)))