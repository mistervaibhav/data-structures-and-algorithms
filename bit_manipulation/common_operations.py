def get_bit_at_position(number,position):
    # left shift 1 by i
    mask = 1 << position
    # & mask and number
    result = number & mask
    if result > 0:
        return 1
    return 0
 

def set_bit_at_position(number,position):
    pass


def clear_bit_at_position(number,position):
    pass