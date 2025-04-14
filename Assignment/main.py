num = int(input("Enter a number: "))

# Get the binary representation (remove '0b' prefix)
binary = bin(num)[2:]

# Reverse the binary string
reversed_binary = binary[::-1]

# Convert back to integer
reversed_num = int(reversed_binary, 2)

print(f"Reversed bits number: {reversed_num}")
