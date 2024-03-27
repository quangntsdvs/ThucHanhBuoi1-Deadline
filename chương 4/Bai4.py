class BT:
    def __init__(self):
        self.result = []

    def HauTo(self, bt):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        stack = []
        for char in bt:
            if char.isdigit():
                self.result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    self.result.append(stack.pop())
                stack.pop() 
            elif char in precedence:
                while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                    self.result.append(stack.pop())
                stack.append(char)
        while stack:
            self.result.append(stack.pop())
        return ' '.join(self.result)

bt = input("Nhập biểu thức số học: ")
expression = BT()
result = expression.HauTo(bt)
print("Biểu thức hậu tố:", result)