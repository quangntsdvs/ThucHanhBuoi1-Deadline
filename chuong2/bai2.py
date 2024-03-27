def TamGiacTren(matrix):
    n = len(matrix)
    for i in range(1, n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

def main():
    n = int(input("Kích thước của ma trận vuông n = "))
    matrix = []
    print("Nhập các phần tử của ma trận (cách nhau bởi dấu cách): ")
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Số lượng phần tử không đúng. Nhập lại.")
            return
        matrix.append(row)

    if TamGiacTren(matrix):
        print("Ma trận là ma trận tam giác trên.")
    else:
        print("Ma trận không phải là ma trận tam giác trên.")

if __name__ == "__main__":
    main()
