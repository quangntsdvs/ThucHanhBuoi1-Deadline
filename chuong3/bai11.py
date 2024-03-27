class Node:
    def __init__(self, he_so, so_mu):
        self.he_so = he_so
        self.so_mu = so_mu
        self.ke_tiep = None
class DanhThuc:
    def __init__(self):
        self.head = None
    def them_so_hang(self, he_so, so_mu):
        if self.head is None:
            self.head = Node(he_so, so_mu)
        else:
            current = self.head
            while current.ke_tiep is not None:
                current = current.ke_tiep
            current.ke_tiep = Node(he_so, so_mu)
    def Tich(self, dathuc2):
        result_dathuc = DanhThuc()
        current1 = self.head
        while current1 is not None:
            current2 = dathuc2.head
            while current2 is not None:
                he_so_moi = current1.he_so * current2.he_so
                so_mu_moi = current1.so_mu + current2.so_mu
                result_dathuc.them_so_hang(he_so_moi, so_mu_moi)
                current2 = current2.ke_tiep
            current1 = current1.ke_tiep

        result_dathuc.RutGon()
        return result_dathuc
    def RutGon(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            next_node = current.ke_tiep
            while next_node is not None:
                if next_node.so_mu == current.so_mu:
                    current.he_so += next_node.he_so
                    current.ke_tiep = next_node.ke_tiep
                    next_node = current.ke_tiep
                else:
                    next_node = next_node.ke_tiep
            current = current.ke_tiep
        prev = None
        current = self.head
        while current is not None:
            if current.he_so == 0:
                if prev is None:
                    self.head = current.ke_tiep
                else:
                    prev.ke_tiep = current.ke_tiep
            else:
                prev = current
            current = current.ke_tiep

    def in_danh_thuc(self):
        if self.head is None:
            print("Danh sách liên kết trống.")
            return

        current = self.head
        while current is not None:
            print(f"{current.he_so}x^{current.so_mu}", end="")
            current = current.ke_tiep
            if current is not None:
                print(" + ", end="")
        print()
# ví dụ
dathuc1 = DanhThuc()
dathuc1.them_so_hang(3, 2)
dathuc1.them_so_hang(4, 1)
dathuc1.them_so_hang(2, 0)

dathuc2 = DanhThuc()
dathuc2.them_so_hang(2, 3)
dathuc2.them_so_hang(5, 1)
dathuc2.them_so_hang(1, 0)

print("Danh thức 1:")
dathuc1.in_danh_thuc()

print("Danh thức 2:")
dathuc2.in_danh_thuc()

ket_qua = dathuc1.Tich(dathuc2)

print("Kết quả:")
ket_qua.in_danh_thuc()
