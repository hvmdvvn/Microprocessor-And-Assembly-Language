# ISA Simulator in Python

# Memory (M0-M15) and Registers (R0-R15)
memory = [10, 20, 30, 40, 50, 60, 70, 80, 90, 30, 50, 60, 70, 80, 90, 10]
registers = [0] * 16

# Instruction Memory (2D array)
instruction_memory = []

# Opcodes
LOAD = 1
STORE = 3
ADD = 5

def print_state():
    # Print Registers
    print("Register:", end=" ")
    for r in registers:
        print(f"{r:2}", end=" ")
    print()

    # Print Memory
    print("Memory:  ", end=" ")
    for m in memory:
        print(f"{m:2}", end=" ")
    print()
    print("#" * 70)

# Input
n = int(input("Enter number of instructions: "))

for i in range(n):
    print(f"\nEnter Instruction #{i+1}")
    print("Instruction Type (1=LOAD, 3=STORE, 5=ADD): ", end="")
    instr = int(input())
    op1 = int(input("Operand #1 (Register Number): "))
    op2 = int(input("Operand #2 (Register/Memory): "))
    instruction_memory.append([instr, op1, op2])

    if instr == LOAD:  # If LOAD, also set memory value
        val = int(input(f"Enter value at Memory M{op2}: "))
        memory[op2] = val

print("\n**************************** ISA Simulator ****************************\n")

# Simulation Cycle by Cycle
for cycle, instr in enumerate(instruction_memory, 1):
    opcode, op1, op2 = instr
    print(f"**************************** Cycle # {cycle} ****************************")

    # FETCH
    fetch_str = f"{opcode} {op1} {op2}"

    # DECODE
    if opcode == LOAD:
        decode_str = f"LOAD\nRegister R{op1}\nMemory M{op2}"
    elif opcode == STORE:
        decode_str = f"STORE\nRegister R{op1}\nMemory M{op2}"
    elif opcode == ADD:
        decode_str = f"ADD\nRegister R{op1}\nRegister R{op2}"
    else:
        decode_str = "Unknown"

    # EXECUTE
    if opcode == LOAD:
        registers[op1] = memory[op2]
        exec_str = "Register Updated"
    elif opcode == STORE:
        memory[op2] = registers[op1]
        exec_str = "Memory Updated"
    elif opcode == ADD:
        registers[op1] = registers[op1] + registers[op2]
        exec_str = "Register Updated"
    else:
        exec_str = "Invalid instruction"

    # Print table-like output
    print(f"{'Fetch Instruction':<25}{'Decode Instruction':<25}{'Execute Instruction'}")
    print(f"{fetch_str:<25}{decode_str:<25}{exec_str}")
    print()
    print_state()
