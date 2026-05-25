Number = int(input("Enter a number: "))

result = 1
for i in range(1, Number + 1):
    result *= i

print (f"Factorial of {Number} is {result}")