import random

def middle_square(n):
    """
    Generates n values using the middle-square pseudo-random number generator.

    Starting from a 4-digit seed, each step squares the current value, pads the
    result to 8 digits, and extracts the middle four digits to form the next
    state. The function returns both the generated values and a concatenated
    binary representation of those values.
    """
    seed = random.randint(1000, 9999) # 4 digit seed
    number = seed
    bits = ""
    number_list = []

    for _ in range(n):
        number = (int(str(number * number).zfill(8)[2:6]))
        number_list.append(number)

        bits += format(number, '014b') # 4 digit numbers ~ 14 bits

        # exception case for collapsing to 0
        if number == 0:
            number = random.randint(1000, 9999)
       
    return bits, number_list
        
        
        
