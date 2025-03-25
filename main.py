num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number.")
elif num == 0:
    print(num, "is neither positive nor negative, it is zero.")
else:
    print(num, "is a negative number.")

print("Outside body of if statement")