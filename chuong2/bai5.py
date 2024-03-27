def Cong(a, b):
    str_a = ''.join(map(str, a))
    str_b = ''.join(map(str, b))
    result = int(str_a) + int(str_b)
    if result > (2 ** 32) - 1:
        return [-1] * len(a)
    else:
        return result

def main():
    a = list(map(int, input("Nhập số nguyên không dấu a = ")))
    b = list(map(int, input("Nhập số nguyên không dấu b = ")))
    result = Cong(a, b)
    if isinstance(result, list) and result[0] == -1:
        print("Kết quả bị tràn.")
    else:
        print("a + b = ", result)

if __name__ == "__main__":
    main()
