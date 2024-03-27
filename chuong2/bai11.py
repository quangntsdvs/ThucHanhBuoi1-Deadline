def Cong(a, b):
    result_sign = a[0]
    max_num = max(a[1], b[1])
    min_num = min(a[1], b[1])
    if a[0] == b[0]:
        result_number = cong_so_duong(max_num, min_num)
        if result_number == [0]:
            result_sign = 0
    else:
        result_number = tru_so_duong(max_num, min_num)
    if result_number != [-1]:
        return (result_sign, result_number)
    else:
        return [-1]
def cong_so_duong(a, b):
    result = []
    carry = 0 
    max_len = max(len(a), len(b))
    a = [0] * (max_len - len(a)) + a
    b = [0] * (max_len - len(b)) + b
    for i in range(max_len - 1, -1, -1):
        sum_digit = a[i] + b[i] + carry
        result.insert(0, sum_digit % 10)
        carry = sum_digit // 10
    if carry:
        result.insert(0, carry)
    return result
def tru_so_duong(a, b):
    result = []
    borrow = 0  
    for i in range(len(a) - 1, -1, -1):
        diff_digit = a[i] - b[i] - borrow

        if diff_digit < 0:
            diff_digit += 10
            borrow = 1
        else:
            borrow = 0
        result.insert(0, diff_digit)
    while result[0] == 0 and len(result) > 1:
        del result[0]
    return result
