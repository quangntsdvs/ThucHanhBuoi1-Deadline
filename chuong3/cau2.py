class Node:
    def __init__(self, HeSo, SoMu):
        self.HeSo = HeSo
        self.SoMu = SoMu
        self.KeTiep = None

class DanhSachDaThuc:
    def __init__(self):
        self.Head = None

    def ThemSoHang(self, HeSo, SoMu):
        if self.Head is None:
            self.Head = Node(HeSo, SoMu)
        else:
            current = self.Head
            while current.KeTiep is not None:
                current = current.KeTiep
            current.KeTiep = Node(HeSo, SoMu)

    def RutGon(self):
        if self.Head is None:
            return

        current = self.Head
        while current is not None:
            temp = current.KeTiep
            while temp is not None:
                if temp.SoMu == current.SoMu:
                    current.HeSo += temp.HeSo
                    temp.HeSo = 0 
                temp = temp.KeTiep
            current = current.KeTiep

        prev = None
        current = self.Head
        while current is not None:
            if current.HeSo == 0:
                if prev is None:
                    self.Head = current.KeTiep
                else:
                    prev.KeTiep = current.KeTiep
            else:
                prev = current
            current = current.KeTiep

    def XuatDaThuc(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep
        print()

def main():
    dathuc = DanhSachDaThuc()
    n = int(input("Nhập số hạng của đa thức: "))
    for i in range(n):
        HeSo = float(input(f"Nhập hệ số của số hạng {i+1}: "))
        SoMu = int(input(f"Nhập số mũ của số hạng {i+1}: "))
        dathuc.ThemSoHang(HeSo, SoMu)

    print("Đa thức có dạng:")
    dathuc.XuatDaThuc()

    dathuc.RutGon()

    print("Đa thức rút gọn:")
    dathuc.XuatDaThuc()

if __name__ == "__main__":
    main()
