#https://www.codewars.com/kata/58e24788e24ddee28e000053

def simple_assembler(program):
    registers = {}
    pointer = 0  
    
    while pointer < len(program):
        instruction = program[pointer].split()
        command = instruction[0]
        
        if command == "mov":
            reg, val = instruction[1], instruction[2]
            registers[reg] = int(val) if val.lstrip('-').isdigit() else registers[val]
        elif command == "inc":
            reg = instruction[1]
            registers[reg] += 1
        elif command == "dec":
            reg = instruction[1]
            registers[reg] -= 1
        elif command == "jnz":
            val, offset = instruction[1], int(instruction[2])
            val = int(val) if val.lstrip('-').isdigit() else registers[val]
            if val != 0:
                pointer += offset
                continue  
        pointer += 1
    
    return registers