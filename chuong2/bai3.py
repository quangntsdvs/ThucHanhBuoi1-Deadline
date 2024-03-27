def TrungHang(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i] == matrix[j]:
                return True
    return False

def main():
    n = int(input("Nhập Kích thước của ma trận vuông n = "))
    matrix = []
    print("Nhập các phần tử của ma trận: ")
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Số lượng phần tử không đúng. Nhập lại.")
            return
        matrix.append(row)

    if TrungHang(matrix):
        print("Ma trận có ít nhất hai hàng giống nhau.")
    else:
        print("Ma trận không hàng giống nhau.")

if __name__ == "__main__":
    main()
