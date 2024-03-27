def DayConDaiNhat(a, b):
    max_length = 0  
    max_subarray = []  
    for i in range(len(a)):
        for j in range(len(b)):
            length = 0
            subarray = []
            while i < len(a) and j < len(b) and a[i] == b[j]:
                subarray.append(a[i])
                length += 1
                i += 1
                j += 1
            if length > max_length:
                max_length = length
                max_subarray = subarray.copy()
    return max_subarray
# ví dụ
a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
c = DayConDaiNhat(a, b)
print("Dãy con có chiều dài lớn nhất:", c)
