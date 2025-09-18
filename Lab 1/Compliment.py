def OnesCompliment(integer_str):
    integer_value = int(integer_str)
    if integer_value < 0:
        raise ValueError("Input must be a non-negative integer.")
    binary_value = bin(integer_value)[2:]  # Convert to binary and remove '0b' prefix
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_value)
    return ones_complement

def TwosCompliment(integer_str):
    integer_value = int(integer_str)
    if integer_value < 0:
        raise ValueError("Input must be a non-negative integer.")
    binary_value = bin(integer_value)[2:]  # Convert to binary and remove '0b' prefix
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_value)
    # Add 1 to the one's complement
    twos_complement_int = int(ones_complement, 2) + 1
    twos_complement = bin(twos_complement_int)[2:]  # Convert back to binary and remove '0b' prefix
    return twos_complement

user_input = input("Enter a non-negative integer: ")
ones_complement, twos_complement = OnesCompliment(user_input), TwosCompliment(user_input)
print("One's Complement:", ones_complement)
print("Two's Complement:", twos_complement)
