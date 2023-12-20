#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for counter in range(1, 3):
        try:
            if counter > a:
                raise Exception('Too far')
            else:
                result += a ** b / counter
        except Exception:
            result = b + a
            break
    return result
