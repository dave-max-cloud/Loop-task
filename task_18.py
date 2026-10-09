number = int(input("Enter a number:"))
digit = 0

while number > 0:
    last_digit = number % 10
    digit += last_digit
    number //= 10
print(f"The sum of is:{digit}")
