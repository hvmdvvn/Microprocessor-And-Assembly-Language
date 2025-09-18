def Base2To16(binary_str):
    result = 0
    binary_str = binary_str[::-1]
    for index, digit in enumerate(binary_str):
        if digit == '1':
            result += 2 ** index
    hex_value = hex(result)[2:].upper()
    return hex_value

