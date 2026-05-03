import dis
 
def check_even_odd(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append("even")
        else:
            result.append("odd")
    return result
 
print("===Bytecode===")
dis.dis(check_even_odd)