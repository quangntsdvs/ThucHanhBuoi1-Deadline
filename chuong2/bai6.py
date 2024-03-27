def Tru(a, b):
    str_a = ''.join(map(str, a))
    str_b = ''.join(map(str, b))
    
    if int(str_a) < int(str_b):
        raise ValueError("Sai điều kiện. Nhập lại")
        
    result = int(str_a) - int(str_b)
    return result

def main():
    print("Điều kiện a >= b")
    a = list(map(int, input("Nhập số nguyên không dấu a: ")))
    b = list(map(int, input("Nhập số nguyên không dấu b: ")))
    
    try:
        result = Tru(a, b)
        print("Kết quả của a - b = ", result)
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()
