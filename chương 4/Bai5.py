class HanoiTower:
    def move(self, n, source, target, auxiliary):
        if n == 1:
            print("Di chuyển tầng 1 từ tháp", source, "đến tháp", target)
            return
        self.move(n - 1, source, auxiliary, target)
        print("Di chuyển tầng", n, "từ tháp", source, "đến tháp", target)
        self.move(n - 1, auxiliary, target, source)

tower = HanoiTower()
n = int(input("Nhập số tầng của tháp: "))
print("Bước di chuyển:")
tower.move(n, '1', '3', '2')