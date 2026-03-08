import random

def middle_square(n):
    """
    Generates n values using the middle-square pseudo-random number generator.

    Starting from a 4-digit seed, each step squares the current value, pads the
    result to 8 digits, and extracts the middle four digits to form the next
    state. The function returns both the generated values and a concatenated
    14-bit binary representation of those values.
    """
    seed = random.randint(1000, 9999)
    number = seed
    bits = ""
    number_list = []

    for _ in range(n):
        number = (int(str(number * number).zfill(8)[2:6]))
        number_list.append(number)
        bits += format(number, '014b')
       
    return bits, number_list
        
        
        
