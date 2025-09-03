def HexToDec(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_num

def HexToBin(hex_num):
    decimal_num = HexToDec(hex_num)
    binary_num = bin(decimal_num)[2:]  # Remove the '0b' prefix
    return binary_num

def HexToOct(hex_num):
    decimal_num = HexToDec(hex_num)
    octal_num = oct(decimal_num)[2:]  # Remove the '0o' prefix
    return octal_num

user_input = input("Enter a hexadecimal number: ")
decimal, binary, octal = HexToDec(user_input), HexToBin(user_input), HexToOct(user_input)

print("Decimal:", decimal)
print("Binary:", binary)
print("Octal:", octal)