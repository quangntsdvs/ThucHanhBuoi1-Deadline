class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class DSLK:
    def __init__(self):
        self.head = None
    
    def Them(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    
    def DaoNguoc(self):
        if self.head is None:
            return
        
        stack = []
        current = self.head
        while current:
            stack.append(current)
            current = current.next
        
        self.head = stack.pop()
        current = self.head
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None
    
    def InDanhSach(self):
        current = self.head
        while current:
            print(current.info, end=" ")
            current = current.next
        print()

dslk = DSLK()
n = int(input("Nhập số lượng phần tử: "))
print("Nhập các phần tử:")
for _ in range(n):
    value = int(input())
    dslk.Them(value)

print("Danh sách liên kết ban đầu:")
dslk.InDanhSach()

print("Danh sách liên kết sau khi đảo ngược:")
dslk.DaoNguoc()
dslk.InDanhSach()