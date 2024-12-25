def rebase(input_base, digits, output_base):
    if(input_base < 2):
        raise ValueError("input base must be >= 2")

    if(output_base < 2):
        raise ValueError("output base must be >= 2")

    for x in digits:
        if not(0 <= x < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if input_base == 10:
        return decimal_to_base(digits, output_base)
    if output_base == 10:
        return num_to_arr(base_to_decimal(digits, input_base))

    dec = base_to_decimal(digits, input_base)

    return decimal_to_base(num_to_arr(dec), output_base)

def base_to_decimal(digits, base):
    result=0
    # print(list(range(len(digits))))
    # print(list(range(len(digits) - 1, -1, -1)))
    digits.reverse()
    for x in range(len(digits) - 1, -1, -1):
        result += digits[x] * (base ** x)

    return result


# def from_decimal(digits, base):
#     print(digits, base, "p")
#     # num = int("".join(map(str, digits)))
#     num = int("".join(map(str, digits)))

#     return get_remainders(num, base)


def decimal_to_base(digits, base):
    """Converts a decimal number to the specified base."""

    decimal_num = int("".join(map(str, digits)))

    if decimal_num == 0:
        return [0]

    result = []

    while decimal_num > 0:
        remainder = decimal_num % base
        result.insert(0, remainder)
        decimal_num //= base

    return result


# def get_remainders(num, base, current_list = []):

#     new_num = round(num / base)
#     new_list = current_list.copy()
#     new_list.insert(0, round(num % base))
#     print(base, new_num)
#     if base <= new_num and new_num != new_list[0]:
        

#         return get_remainders(new_num, base, new_list)
#         print(current_list)

#     if new_num == current_list[0]:
#             return int( "".join(map(str, current_list + [new_num] )))

#     return int( "".join(map(str, current_list)))


# def num_to_arr(num):
#     return list(map(int, list(str(num))))


