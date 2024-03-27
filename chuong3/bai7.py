class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DanhSachDaThuc:
    def __init__(self):
        self.head = Node(None, None)  
        self.head.KeTiep = self.head

    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        current = self.head
        while current.KeTiep != self.head:
            current = current.KeTiep
        current.KeTiep = new_node
        new_node.KeTiep = self.head

    def XuatDaThuc(self):
        current = self.head.KeTiep 
        while current != self.head:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            if current.KeTiep != self.head:
                print("+", end=" ")
            current = current.KeTiep
        print()

def main():
    dathuc = DanhSachDaThuc()
    while True:
        heso = float(input("hệ số (để kết thúc nhập 0): "))
        if heso == 0:
            break
        somu = int(input("số mũ : "))
        dathuc.Them(heso, somu)

    print("Đa thức có dạndạng:")
    dathuc.XuatDaThuc()

if __name__ == "__main__":
    main()
