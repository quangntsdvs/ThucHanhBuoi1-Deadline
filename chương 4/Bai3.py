class BT:
    def __init__(self):
        self.operands = []
        self.operators = []

    def GiaTri(self, bt):
        for char in bt:
            if char.isdigit():
                self.operands.append(int(char))
            elif char in '+-*/':
                while self.operators and self.precedence(char) <= self.precedence(self.operators[-1]):
                    self.process_operator()
                self.operators.append(char)
            elif char == '(':
                self.operators.append(char)
            elif char == ')':
                while self.operators[-1] != '(':
                    self.process_operator()
                self.operators.pop()

        while self.operators:
            self.process_operator()

        return self.operands[-1]

    def precedence(self, operator):
        if operator in '+-':
            return 1
        elif operator in '*/':
            return 2
        return 0

    def process_operator(self):
        operator = self.operators.pop()
        operand2 = self.operands.pop()
        operand1 = self.operands.pop()
        if operator == '+':
            self.operands.append(operand1 + operand2)
        elif operator == '-':
            self.operands.append(operand1 - operand2)
        elif operator == '*':
            self.operands.append(operand1 * operand2)
        elif operator == '/':
            self.operands.append(operand1 / operand2)

bt = input("Nhập biểu thức số học: ")
expression = BT()
result = expression.GiaTri(bt)
print("Giá trị của biểu thức là:", result)