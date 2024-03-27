def TrungCot(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            cot_i = [matrix[x][i] for x in range(n)]
            cot_j = [matrix[x][j] for x in range(n)]
            if cot_i == cot_j:
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

    if TrungCot(matrix):
        print("Ma trận có ít nhất hai cột giống nhau.")
    else:
        print("Ma trận không có cột nào giống nhau.")

if __name__ == "__main__":
    main()
