divisor = int(input("Enter a number to find it's divisor: "))

try:
    result = 10/divisor
    print(result)
except ZeroDivisionError:
    print("Error:Division by zero.")
finally:
    print("Finished running")