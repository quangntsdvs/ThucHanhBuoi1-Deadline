def DayConDauTien(a, b):
    set_a = set()
    result = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            set_a.add(tuple(a[i:j+1]))
    for i in range(len(b)):
        for j in range(i, len(b)):
            subarray = tuple(b[i:j+1])
            if subarray in set_a:
                result = list(subarray)
                return result
    
    return result
# ví dụ
a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 8]

result = DayConDauTien(a, b)
print("Dãy con chung đầu tiên là:", result)
