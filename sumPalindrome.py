#Write a Python program to reverse the digits of a given number and add them to the original. If the sum is not a palindrome, repeat this procedure.

def reverse_number(number):
    return int(str(number)[::-1])

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def reverse_and_add_to_palindrome(number):
    while True:
        reversed_num = reverse_number(number)
        number += reversed_num
        if is_palindrome(number):
            return number

# Test the function
num = int(input("Enter a number: "))
result = reverse_and_add_to_palindrome(num)
print("Palindrome obtained by reversing and adding digits:", result)
