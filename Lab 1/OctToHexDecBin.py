def OctToHex(octal_str):
    decimal = int(octal_str, 8)
    hexadecimal = hex(decimal)[2:].upper()
    return hexadecimal

def OctToDec(octal_str):
    decimal = int(octal_str, 8)
    return decimal

def OctToBin(octal_str):
    decimal = int(octal_str, 8)
    binary = bin(decimal)[2:]
    return binary

user_input = input("Enter an octal number: ")
hexadecimal, decimal, binary = OctToHex(user_input), OctToDec(user_input), OctToBin(user_input)
print("Hexadecimal:", hexadecimal)
print("Decimal:", decimal)
print("Binary:", binary)