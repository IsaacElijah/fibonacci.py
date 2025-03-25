# Ask the user for their name
name = input("Enter your name: ")

# Greet the user
print(f"Hello, {name}!")

# Ask how they are doing
response = input("How are you doing today? ")

# Respond based on their input
if response.lower() in ["good", "great", "fine", "well", "okay"]:
    print("That's wonderful to hear!")
else:
    print("I hope your day gets better!")