def Is_fibonacci(n):
    x, y = 0, 1
    while x < n:
        x, y = y, x + y
    return x == n

def main():
    numbers = []
    
    while True:
        try:
            num = int(input("Enter a number (negative to exit): "))
            if num < 0:
                break
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    fibonacci_numbers = [num for num in numbers if Is_fibonacci(num)]

    print("Count of Fibonacci numbers:", len(fibonacci_numbers))
    if (len(fibonacci_numbers)==0):
        print("Error: No fibonacci number is found")

if __name__ == "__main__":
    main()
# added a comment
