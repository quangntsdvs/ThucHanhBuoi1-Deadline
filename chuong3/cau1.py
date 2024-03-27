class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DanhSachDaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        if self.head is None:
            self.head = Node(heso, somu)
        else:
            current = self.head
            while current.KeTiep is not None:
                current = current.KeTiep
            current.KeTiep = Node(heso, somu)

    def XuatDaThuc(self):
        current = self.head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end =" ")
            if current.KeTiep is not None:
                print("+", end =" ")
            current = current.KeTiep
        print()

def main():
    dathuc = DanhSachDaThuc()
    while True:
        heso = float(input("Hệ số (để kết thúc nhập 0): "))
        if heso == 0:
            break
        somu = int(input("số mũ: "))
        dathuc.Them(heso, somu)

    print("Đa thức có dạng:")
    dathuc.XuatDaThuc()

if __name__ == "__main__":
    main()
