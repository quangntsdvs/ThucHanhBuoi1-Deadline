def TamGiacDuoi(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False
    return True

def main():
    n = int(input("Nhập kích thước của ma trận vuông n = "))
    matrix = []
    print("Nhập các phần tử của ma trận:")
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Số lượng phần tử không đúng. Nhập lại.")
            return
        matrix.append(row)

    if TamGiacDuoi(matrix):
        print("Ma trận là ma trận tam giác dưới.")
    else:
        print("Ma trận không phải là ma trận tam giác dưới.")

if __name__ == "__main__":
    main()
