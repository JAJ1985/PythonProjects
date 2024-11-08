def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)

    # Reverse the string
    reversed_str = num_str[::-1]

    # Check if the reversed string is equal to the original string.
    if num_str == reversed_str:
        return True
    else:
        return False


 # Take input from user
num = int(input('Enter a number: '))

# Check if the number is a palindrome or not
if is_palindrome(num):
    print(num, 'is a palindrome')
else:
    print(num, 'is not a palindrome')
