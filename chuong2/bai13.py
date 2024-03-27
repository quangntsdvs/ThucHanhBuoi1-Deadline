def nhap_so():
    sign = int(input("Nhập phần dấu của số (0 cho dương, 1 cho âm): "))
    number = input("Nhập phần số của số (các chữ số cách nhau bằng khoảng trắng): ").split()
    return (sign, [int(x) for x in number])

def Nhan(a, b):
    # Tính phần dấu của kết quả
    result_sign = a[0] ^ b[0]  # XOR để xác định phần dấu của kết quả

    # Tính phần số của kết quả
    result_number = nhan_so(a[1], b[1])

    # Kiểm tra kết quả có tràn không
    if result_number != [-1]:
        return (result_sign, result_number)
    else:
        return [-1]

def nhan_so(a, b):
    # Tính toán phần số của kết quả
    result = [0] * (len(a) + len(b))  # Khởi tạo mảng kết quả với các giá trị ban đầu là 0

    # Thực hiện phép nhân từ cuối mảng số
    for i in range(len(a) - 1, -1, -1):
        carry = 0
        for j in range(len(b) - 1, -1, -1):
            # Thực hiện phép nhân và cộng vào kết quả tương ứng
            mul = a[i] * b[j] + carry + result[i + j + 1]
            result[i + j + 1] = mul % 10
            carry = mul // 10
        result[i] += carry  # Thêm carry vào phần tử đầu tiên của phép nhân

    # Kiểm tra xem kết quả có tràn không
    if result[0] == 0 or result[0] == 1:
        return result
    else:
        return [-1]

# Nhập số a từ bàn phím
a = nhap_so()

# Nhập số b từ bàn phím
b = nhap_so()

# Thực hiện phép nhân và in kết quả
result = Nhan(a, b)
if result == [-1]:
    print("Kết quả bị tràn")
else:
    print("Kết quả của phép nhân là:", result[0], result[1])
