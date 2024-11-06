#Write a function to find the factorial of a number but also store the factorials calculated in a dictionary.

dfactorials = {}

def factorial(n):
  
    if n < 0:
        raise ValueError("No negative values allowed")
    
    if n in dfactorials:
        return dfactorials[n]
    
    if n == 0 or n == 1:
        dfactorials[n] = 1
    else:
        dfactorials[n] = n * factorial(n - 1)
    
    return dfactorials[n]

def main():
    while True:
        print("\nMenu")
        print("1. Calculate factorial")
        print("2. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                number = int(input("Enter the number: "))
                result = factorial(number)
                print(f"Factorial of {number} is {result}")
                print("Factorial Dictionary:", dfactorials)
            except ValueError as e:
                print(e)
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1 or 2).")

if __name__ == "__main__":
    main()
