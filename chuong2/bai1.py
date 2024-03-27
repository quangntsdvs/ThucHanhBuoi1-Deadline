def DoiXung(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def nhapMaTran():
    n = int(input("Nhập số hàng/cột của ma trận: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Nhập hàng {i + 1} (các số cách nhau bởi dấu cách): ").split()))
        if len(row) != n:
            print("Số lượng phần tử không đúng. Vui lòng nhập lại.")
            return nhapMaTran()  
        matrix.append(row)
    return matrix

matrix = nhapMaTran()
if DoiXung(matrix):
    print("Ma trận trên đối xứng")
else:
    print("Ma trận không đối xứng")