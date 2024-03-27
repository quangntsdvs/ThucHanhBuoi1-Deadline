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
    def Tich(self, dathuc2):
        result = DanhSachDaThuc()
        current1 = self.Head
        while current1 is not None:
            current2 = dathuc2.Head
            while current2 is not None:
                result.Them(current1.HeSo * current2.HeSo, current1.SoMu + current2.SoMu)
                current2 = current2.KeTiep
            current1 = current1.KeTiep
        result.RutGon()       
        return result
    def InDaThuc(self):
        current = self.Head
        while current is not None:
            print(current.HeSo, 'x^', current.SoMu, end=' ')
            current = current.KeTiep
        print()
da_thuc1 = DanhSachDaThuc()
while True:
    heso = float(input("Nhập hệ số của số hạng đa thức thứ nhất (nhập 0 để kết thúc): "))
    if heso == 0:
        break
    somu = int(input("Nhập số mũ của số hạng: "))
    da_thuc1.Them(heso, somu)
da_thuc2 = DanhSachDaThuc()
while True:
    heso = float(input("Nhập hệ số của số hạng đa thức thứ hai (nhập 0 để kết thúc): "))
    if heso == 0:
        break
    somu = int(input("Nhập số mũ của số hạng: "))
    da_thuc2.Them(heso, somu)
print("Đa thức 1 trước khi nhân:")
da_thuc1.InDaThuc()
print("Đa thức 2 trước khi nhân:")
da_thuc2.InDaThuc()
da_thuc_tich = da_thuc1.Tich(da_thuc2)
print("Đa thức tổng sau khi nhân:")
da_thuc_tich.InDaThuc()
