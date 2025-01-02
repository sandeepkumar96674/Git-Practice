def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
        user_input = int(input("Enter a number to check if it's a prime number: "))
        if is_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
