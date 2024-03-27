def Dao(mang):
    def dfs(x, y, visited):
        if x < 0 or x >= len(mang) or y < 0 or y >= len(mang[0]) or mang[x][y] == 0 or visited[x][y]:
            return 0
        visited[x][y] = True
        area = 1
        area += dfs(x + 1, y, visited)
        area += dfs(x - 1, y, visited)
        area += dfs(x, y + 1, visited)
        area += dfs(x, y - 1, visited)
        return area
    max_area = 0
    visited = [[False] * len(mang[0]) for _ in range(len(mang))]
    for i in range(len(mang)):
        for j in range(len(mang[0])):
            if mang[i][j] == 1 and not visited[i][j]:
                max_area = max(max_area, dfs(i, j, visited))
    print("Diện tích lớn nhất của các đảo là:", max_area)
# ví dụ
mang = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]
Dao(mang)
