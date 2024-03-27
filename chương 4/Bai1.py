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
    
    def InNguocIterative(self):
        if self.head is None:
            return
        stack = []
        current = self.head
        while current:
            stack.append(current.info)
            current = current.next
        while stack:
            print(stack.pop(), end=" ")

def main():
    dslk = DSLK()

    n = int(input("Nhập số lượng nút của DSLK: "))
    
    print("Nhập dữ liệu cho các nút:")
    for i in range(n):
        data = input("Nút {}: ".format(i+1))
        dslk.Them(data)
    
    print("Danh sách theo thứ tự ngược lại:")
    dslk.InNguocIterative()

if __name__ == "__main__":
    main()