n = int(input("Enter the number"))
counter = n
while n:
    n = int(input("Enter the next number"))
    counter += n
    print(f"The sum of numbers is:{counter}")
