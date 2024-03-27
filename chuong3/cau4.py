class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None
class DanhSachDaThuc:
    def __init__(self):
        self.Head = None
    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.Head is None:
            self.Head = new_node
            return
        if somu >= self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return
        current = self.Head
        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    def RutGon(self):
        if self.Head is None:
            return

        current = self.Head
        while current is not None and current.KeTiep is not None:
            if current.SoMu == current.KeTiep.SoMu:
                current.HeSo += current.KeTiep.HeSo
                current.KeTiep = current.KeTiep.KeTiep
            else:
                current = current.KeTiep
        current = self.Head
        prev = None
        while current is not None:
            if current.HeSo == 0:
                if prev is None:
                    self.Head = current.KeTiep
                else:
                    prev.KeTiep = current.KeTiep
            else:
                prev = current
            current = current.KeTiep

    def DoiDau(self):
        current = self.Head
        while current is not None:
            current.HeSo = -current.HeSo
            current = current.KeTiep

    def InDaThuc(self):
        current = self.Head
        while current is not None:
            print(current.HeSo, 'x^', current.SoMu, end=' ')
            current = current.KeTiep
        print()
da_thuc = DanhSachDaThuc()
while True:
    heso = float(input("Nhập hệ số của số hạng (nhập 0 để kết thúc): "))
    if heso == 0:
        break
    somu = int(input("Nhập số mũ của số hạng: "))
    da_thuc.Them(heso, somu)
print("Đa thức trước khi đổi dấu:")
da_thuc.InDaThuc()
da_thuc.DoiDau()
print("Đa thức sau khi đổi dấu:")
da_thuc.InDaThuc()
