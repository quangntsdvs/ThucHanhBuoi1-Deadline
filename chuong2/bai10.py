def NhomCot(matrix):
    n = len(matrix)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            print("Nhóm cột giống nhau: ", i + 1)
            visited[i] = True
            for j in range(i + 1, n):
                cot_i = [matrix[x][i] for x in range(n)]
                cot_j = [matrix[x][j] for x in range(n)]
                if cot_i == cot_j:
                    print(j + 1)
                    visited[j] = True
            print()

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

    print("Các nhóm cột giống nhau: ")
    NhomCot(matrix)

if __name__ == "__main__":
    main()
