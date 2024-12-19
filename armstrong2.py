def is_armstrong(number):
    # Find the number of digits in the number
    num_digits = len(str(number))
    
    # Initialize sum to 0
    armstrong_sum = 0
    
    # Loop through each digit in the number
    for digit in str(number):
        # Convert the digit to an integer and raise it to the power of the number of digits
        armstrong_sum += int(digit) ** num_digits
    
    # Check if the calculated sum equals the original number
    return armstrong_sum == number

# User input
num = int(input("Enter a number: "))

# Check if the number is Armstrong
if is_armstrong(num):
    print(f'{num} is an Armstrong number.')
else:
    print(f'{num} is not an Armstrong number.')
