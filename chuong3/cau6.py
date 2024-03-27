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
    def chep(self):
        new_polynomial = DanhThuc()
        current = self.head
        while current is not None:
            new_polynomial.them_so_hang(current.he_so, current.so_mu)
            current = current.ke_tiep
        return new_polynomial
    def in_danh_thuc(self):
        current = self.head
        while current is not None:
            print(f"{current.he_so}x^{current.so_mu}", end="")
            current = current.ke_tiep
            if current is not None:
                print(" + ", end="")
        print()
# ví dụ
dathuc = DanhThuc()
dathuc.them_so_hang(3, 2)
dathuc.them_so_hang(4, 1)
dathuc.them_so_hang(2, 0)

print("Danh thức gốc:")
dathuc.in_danh_thuc()
danh_thuc_moi = dathuc.chep()
print("Danh thức mới:")
danh_thuc_moi.in_danh_thuc()
