def DecToHex(decimal_str):
    decimal_value = int(decimal_str)
    hex_value = hex(decimal_value)[2:]  # Remove the '0x' prefix
    return hex_value.upper()  # Return in uppercase for standard hexadecimal representation

def DecToBin(decimal_str):
    decimal_value = int(decimal_str)
    binary_value = bin(decimal_value)[2:]  # Remove the '0b' prefix
    return binary_value

def DecToOct(decimal_str):
    decimal_value = int(decimal_str)
    octal_value = oct(decimal_value)[2:]  # Remove the '0o' prefix
    return octal_value

user_input = input("Enter a decimal number: ")
hexadecimal, binary, octal = DecToHex(user_input), DecToBin(user_input), DecToOct(user_input)
print("Hexadecimal:", hexadecimal)
print("Binary:", binary)
print("Octal:", octal)