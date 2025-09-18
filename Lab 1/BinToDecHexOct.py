def BinToDec(binary_str):
    decimal_value = 0
    binary_str = binary_str[::-1]  # Reverse the string to process from least significant bit
    for index, digit in enumerate(binary_str):
        if digit == '1':
            decimal_value += 2 ** index
    return decimal_value

def BinToHex(binary_str):
    decimal_value = BinToDec(binary_str)
    hex_value = hex(decimal_value)[2:]  # Remove the '0x' prefix
    return hex_value.upper()  # Return in uppercase for standard hexadecimal representation

def BinToOct(binary_str):
    decimal_value = BinToDec(binary_str)
    octal_value = oct(decimal_value)[2:]  # Remove the '0o' prefix
    return octal_value

user_input = input("Enter a binary number: ")
decimal, hexadecimal, octal = BinToDec(user_input), BinToHex(user_input), BinToOct(user_input)  
print("Decimal:", decimal)
print("Hexadecimal:", hexadecimal)
print("Octal:", octal)
