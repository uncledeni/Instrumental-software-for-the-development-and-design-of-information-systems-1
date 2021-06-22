from PyQt5 import QtWidgets
import sys
import calculator_interface
import re


class Calc(QtWidgets.QMainWindow, calculator_interface.Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFocus()
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setWindowTitle(self.windowTitle())
        self.stack_of_numbers = []
        self.stack_of_operations = []
        self.operations_priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 0, ")": 0}
        self.operations = {"+": self.sum, "-": self.sub, "*": self.mul, "/": self.div, "^": self.exp}

        self.Zero_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("0"))
        self.Dot_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("."))
        self.Equal_Button.clicked.connect(lambda: self.calculate(self.ExpressionLineEdit.text()))
        self.Plus_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("+"))
        self.Minus_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("-"))
        self.One_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("1"))
        self.Two_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("2"))
        self.Three_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("3"))
        self.Mult_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("*"))
        self.Div_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("/"))
        self.Four_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("4"))
        self.Five_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("5"))
        self.Six_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("6"))
        self.LeftBracket_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("("))
        self.RightBracket_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert(")"))
        self.Seven_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("7"))
        self.Eight_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("8"))
        self.Nine_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("9"))
        self.Exp_Button.clicked.connect(lambda: self.ExpressionLineEdit.insert("^"))
        self.Del_Button.clicked.connect(lambda: self.ExpressionLineEdit.backspace())
        self.Clear_Button.clicked.connect(lambda: self.ExpressionLineEdit.clear())
        self.Exit_Button.clicked.connect(self.close)

        self.Zero_Button.setShortcut("0")
        self.Dot_Button.setShortcut(".")
        self.Equal_Button.setShortcut("=")
        self.Plus_Button.setShortcut("+")
        self.Minus_Button.setShortcut("-")
        self.One_Button.setShortcut("1")
        self.Two_Button.setShortcut("2")
        self.Three_Button.setShortcut("3")
        self.Mult_Button.setShortcut("*")
        self.Div_Button.setShortcut("/")
        self.Four_Button.setShortcut("4")
        self.Five_Button.setShortcut("5")
        self.Six_Button.setShortcut("6")
        self.LeftBracket_Button.setShortcut("(")
        self.RightBracket_Button.setShortcut(")")
        self.Seven_Button.setShortcut("7")
        self.Eight_Button.setShortcut("8")
        self.Nine_Button.setShortcut("9")
        self.Exp_Button.setShortcut("^")
        self.Del_Button.setShortcut("Backspace")
        self.Clear_Button.setShortcut("CTRL+C")
        self.Exit_Button.setShortcut("ESC")

    def sum(self) -> None:
        b = self.stack_of_numbers.pop()
        a = self.stack_of_numbers.pop()
        self.stack_of_numbers.append(float(a) + float(b))
        if self.get_top_of_the_stack(self.stack_of_operations) == "+":
            self.stack_of_operations.pop()

    def sub(self) -> None:
        b = self.stack_of_numbers.pop()
        a = self.stack_of_numbers.pop()
        self.stack_of_numbers.append(float(a) - float(b))
        if self.get_top_of_the_stack(self.stack_of_operations) == "-":
            self.stack_of_operations.pop()

    def mul(self) -> None:
        b = self.stack_of_numbers.pop()
        a = self.stack_of_numbers.pop()
        self.stack_of_numbers.append(float(a) * float(b))
        if self.get_top_of_the_stack(self.stack_of_operations) == "*":
            self.stack_of_operations.pop()

    def div(self) -> None:
        b = self.stack_of_numbers.pop()
        a = self.stack_of_numbers.pop()
        self.stack_of_numbers.append(float(a) / float(b))
        if self.get_top_of_the_stack(self.stack_of_operations) == "/":
            self.stack_of_operations.pop()

    def exp(self) -> None:
        b = self.stack_of_numbers.pop()
        a = self.stack_of_numbers.pop()
        self.stack_of_numbers.append(float(a) ** float(b))
        if self.get_top_of_the_stack(self.stack_of_operations) == "^":
            self.stack_of_operations.pop()

    @staticmethod
    def get_top_of_the_stack(stack: list) -> str:
        return stack[len(stack) - 1]

    @staticmethod
    def get_tokens(expression: str) -> list:
        raw_list = re.split(r"(\D)", expression)
        tokens_list = []
        for i in raw_list:
            if i != " " and i != "":
                if i == ".":
                    tokens_list[len(tokens_list) - 1] += i
                    tokens_list.append(i)
                elif len(tokens_list) > 0 and tokens_list[len(tokens_list) - 1] == ".":
                    tokens_list.pop()
                    tokens_list[len(tokens_list) - 1] += i
                else:
                    tokens_list.append(i)
        return tokens_list

    def calculate(self, expression: str) -> None:
        self.stack_of_numbers.clear()
        self.stack_of_operations.clear()
        tokens = self.get_tokens(expression)
        try:
            for token in tokens:
                if len(self.stack_of_numbers) == 0 and token in self.operations_priority and \
                        (token != '(' and token != ')'):
                    self.stack_of_numbers.append(float(0))
                if tokens.index(token) == len(tokens) - 1 and token in self.operations_priority and \
                        (token != '(' and token != ')'):
                    self.stack_of_numbers.append(float(0))
                if token not in self.operations_priority:
                    self.stack_of_numbers.append(float(token))
                elif len(self.stack_of_operations) > 0 and (token != '(' and token != ')'):
                    while (len(self.stack_of_operations) != 0 and self.operations_priority[token] <=
                           self.operations_priority[self.get_top_of_the_stack(self.stack_of_operations)]):
                        self.operations[self.get_top_of_the_stack(self.stack_of_operations)]()
                    self.stack_of_operations.append(token)
                elif token == ')':
                    self.operations[self.get_top_of_the_stack(self.stack_of_operations)]()
                    self.stack_of_operations.reverse()
                    for i in self.stack_of_operations:
                        if i == '(':
                            self.stack_of_operations.remove(i)
                            break
                    self.stack_of_operations.reverse()
                else:
                    self.stack_of_operations.append(token)
            while len(self.stack_of_operations) != 0:
                self.operations[self.get_top_of_the_stack(self.stack_of_operations)]()
        except (KeyError, IndexError, ValueError, ZeroDivisionError):
            self.msg_box.setText("Ошибка выполнения выражения")
            self.msg_box.exec()
        else:
            if len(self.stack_of_numbers) != 0:
                self.ResultLineEdit.setText(str(self.stack_of_numbers[0]))


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
