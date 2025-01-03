def is_prime(number):
    """
    Check if a number is a prime number.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_palindrome(string):
    """
    Check if a string is a palindrome.

    Parameters:
        string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return string == string[::-1]

def main():
    """
    Main function to take user input and check for prime or palindrome.
    """
    try:
        choice = input("Choose an option: \n1. Check Prime\n2. Check Palindrome\nEnter 1 or 2: ")
        if choice == "1":
            user_input = int(input("Enter a number to check if it's a prime number: "))
            if is_prime(user_input):
                print(f"{user_input} is a prime number.")
            else:
                print(f"{user_input} is not a prime number.")
        elif choice == "2":
            user_input = input("Enter a string to check if it's a palindrome: ")
            if is_palindrome(user_input):
                print(f"'{user_input}' is a palindrome.")
            else:
                print(f"'{user_input}' is not a palindrome.")
        else:
            print("Invalid choice! Please enter 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter the correct data type.")
