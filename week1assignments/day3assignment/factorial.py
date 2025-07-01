"""factorial of 5"""

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def main():
    user_input=int(input(f"\nEnter a number whose factorial is to be found: ").strip())
    print(f"The Factorial of {user_input}  is {factorial(user_input)}")
    return

main()