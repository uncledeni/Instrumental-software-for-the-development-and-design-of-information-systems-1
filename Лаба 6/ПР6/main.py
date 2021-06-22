import codecs
from os.path import splitext
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import TextEditorInterface


class TextEditor(QtWidgets.QMainWindow, TextEditorInterface.Ui_TextEditor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_file = None
        self.html_extensions = [".html", ".htm", ".php", ".aspx", ".asp", ".jsp"]
        font_sizes = ["8", "9", "10", "11", "12", "14", "16", "18", "20", "22", "24", "26", "28", "36", "48", "72"]
        self.colors = {"Black": "#000000",
                       "Blue": "#0000ff",
                       "Green": "#008000",
                       "Red": "#ff0000",
                       }
        self.statusBar.showMessage("Строка: 1 | Столбец: 1 | Позиция: 0 ")
        self.title = self.windowTitle()
        self.resize(800, 600)

        self.TextEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.TextEdit.cursorPositionChanged.connect(self.cursor_position)
        self.TextEdit.selectionChanged.connect(self.update_selection)

        #добавление кнопки "Открыть"
        self.open_file_action = QtWidgets.QAction("Открыть")
        self.open_file_action.triggered.connect(self.open_file)
        self.open_file_action.setShortcut("CTRL+O")
        self.open_file_action.setIcon(QtGui.QIcon("./icons/denis-opened-folder-96.png"))

        # добавление кнопки "Сохранить"
        self.save_file_action = QtWidgets.QAction("Сохранить")
        self.save_file_action.triggered.connect(self.save_file)
        self.save_file_action.setShortcut("CTRL+S")
        self.save_file_action.setIcon(QtGui.QIcon("./icons/denis-save-96.png"))

        # добавление кнопки "Сохранить как"
        self.save_as_file_action = QtWidgets.QAction("Сохранить как")
        self.save_as_file_action.triggered.connect(self.save_as_file)
        self.save_as_file_action.setIcon(QtGui.QIcon("./icons/denis-save-as-96.png"))

        # добавление кнопки "Жирный"
        self.bold_action = QtWidgets.QAction("Жирный")
        self.bold_action.setIcon(QtGui.QIcon("./icons/denis-bold-96.png"))
        self.bold_action.setShortcut("CTRL+B")
        self.bold_action.setCheckable(True)
        self.bold_action.toggled.connect(
            lambda x: self.TextEdit.setFontWeight(QtGui.QFont.Bold if x else QtGui.QFont.Normal))

        # добавление кнопки "Курсив"
        self.italic_action = QtWidgets.QAction("Курсив")
        self.italic_action.setIcon(QtGui.QIcon("./icons/denis-italic-96.png"))
        self.italic_action.setShortcut("CTRL+I")
        self.italic_action.setCheckable(True)
        self.italic_action.toggled.connect(self.TextEdit.setFontItalic)

        # добавление кнопки "Подчёркнутый"
        self.under_line_action = QtWidgets.QAction("Подчёркнутый")
        self.under_line_action.setIcon(QtGui.QIcon("./icons/denis-underline-96.png"))
        self.under_line_action.setShortcut("CTRL+U")
        self.under_line_action.setCheckable(True)
        self.under_line_action.toggled.connect(self.TextEdit.setFontUnderline)

        # добавление кнопки "Перечисляемый список"
        self.bullet_list_action = QtWidgets.QAction("Перечисляемый список")
        self.bullet_list_action.setShortcut("Ctrl+Shift+B")
        self.bullet_list_action.setIcon(QtGui.QIcon("./icons/denis-bulleted-list-96.png"))
        self.bullet_list_action.setCheckable(True)
        self.bullet_list_action.triggered.connect(self.set_bullet_list)

        # добавление кнопки "Вставить нумерованный список"
        self.numbered_list_action = QtWidgets.QAction("Вставить нумерованный список")
        self.numbered_list_action.setIcon(QtGui.QIcon("./icons/denis-numbered-list-96.png"))
        self.numbered_list_action.setShortcut("Ctrl+Shift+L")
        self.numbered_list_action.triggered.connect(self.set_number_list)
        self.numbered_list_action.setCheckable(True)


        self.list_group_action = QtWidgets.QActionGroup(self)
        self.list_group_action.setExclusive(True)
        self.list_group_action.addAction(self.bullet_list_action)
        self.list_group_action.addAction(self.numbered_list_action)

        # добавление кнопки "Выровнять по левому краю"
        self.left_alignment_action = QtWidgets.QAction("Выровнять по левому краю")
        self.left_alignment_action.triggered.connect(
            lambda: self.TextEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft))
        self.left_alignment_action.setIcon(QtGui.QIcon("./icons/denis-align-left-96.png"))
        self.left_alignment_action.setShortcut("CTRL+L")
        self.left_alignment_action.setCheckable(True)

        # добавление кнопки "Выровнять по центру"
        self.center_alignment_action = QtWidgets.QAction("Выровнять по центру")
        self.center_alignment_action.triggered.connect(
            lambda: self.TextEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.center_alignment_action.setIcon(QtGui.QIcon("./icons/denis-align-center-96.png"))
        self.center_alignment_action.setShortcut("CTRL+E")
        self.center_alignment_action.setCheckable(True)

        # добавление кнопки "Выровнять по правому краю"
        self.right_alignment_action = QtWidgets.QAction("Выровнять по правому краю")
        self.right_alignment_action.triggered.connect(
            lambda: self.TextEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight))
        self.right_alignment_action.setIcon(QtGui.QIcon("./icons/denis-align-right-96.png"))
        self.right_alignment_action.setShortcut("CTRL+R")
        self.right_alignment_action.setCheckable(True)

        # добавление кнопки "Выровнять по ширине"
        self.justify_alignment_action = QtWidgets.QAction("Выровнять по ширине")
        self.justify_alignment_action.triggered.connect(
            lambda: self.TextEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify))
        self.justify_alignment_action.setIcon(QtGui.QIcon("./icons/denis-align-justify-96.png"))
        self.justify_alignment_action.setShortcut("CTRL+J")
        self.justify_alignment_action.setCheckable(True)


        self.alignment_group_action = QtWidgets.QActionGroup(self)
        self.alignment_group_action.setExclusive(True)
        self.alignment_group_action.addAction(self.left_alignment_action)
        self.alignment_group_action.addAction(self.right_alignment_action)
        self.alignment_group_action.addAction(self.center_alignment_action)
        self.alignment_group_action.addAction(self.justify_alignment_action)

        # добавление кнопки "Шрифт"
        self.font_combobox = QtWidgets.QFontComboBox()
        self.font_combobox.setToolTip("Шрифт")
        self.font_combobox.setEditable(False)
        self.font_combobox.setCurrentFont(self.TextEdit.currentFont())
        self.font_combobox.currentFontChanged.connect(self.set_font)

        # добавление кнопки "Размер шрифта"
        self.font_size_combobox = QtWidgets.QComboBox()
        self.font_size_combobox.setToolTip("Размер шрифта")
        self.font_size_combobox.setEditable(False)
        self.font_size_combobox.addItems(font_sizes)
        self.font_size_combobox.currentTextChanged.connect(self.set_font_size)

        # добавление кнопки "Цвет текста"
        self.text_color_combobox = QtWidgets.QComboBox()
        self.text_color_combobox.setToolTip("Цвет текста")
        self.text_color_combobox.setEditable(False)
        for color in self.colors:
            self.text_color_combobox.addItem(QtGui.QIcon("./icons/text-color-48.png"), color)
        self.text_color_combobox.currentTextChanged.connect(self.paint_text)

        self.toolBar.addAction(self.open_file_action)
        self.toolBar.addAction(self.save_file_action)
        self.toolBar.addAction(self.save_as_file_action)
        self.toolBar.addSeparator()

        self.toolBar.addWidget(self.font_combobox)
        self.toolBar.addWidget(self.font_size_combobox)
        self.toolBar.addSeparator()

        self.toolBar.addAction(self.bold_action)
        self.toolBar.addAction(self.italic_action)
        self.toolBar.addAction(self.under_line_action)
        self.toolBar.addSeparator()

        self.toolBar.addAction(self.bullet_list_action)
        self.toolBar.addAction(self.numbered_list_action)
        self.toolBar.addSeparator()

        self.toolBar.addAction(self.left_alignment_action)
        self.toolBar.addAction(self.center_alignment_action)
        self.toolBar.addAction(self.right_alignment_action)
        self.toolBar.addAction(self.justify_alignment_action)
        self.toolBar.addSeparator()

        self.toolBar.addWidget(self.text_color_combobox)
        self.format_actions = [
            self.font_combobox,
            self.font_size_combobox,
            self.text_color_combobox,
            self.bold_action,
            self.italic_action,
            self.under_line_action,
        ]
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setWindowTitle(self.windowTitle())
        self.msg_box.setWindowIcon(self.windowIcon())

    def set_win_title(self):
        self.setWindowTitle(self.selected_file + "-" + self.title)

    def set_bullet_list(self) -> None:
        cursor = self.TextEdit.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def set_number_list(self) -> None:
        cursor = self.TextEdit.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    def cursor_position(self) -> None:
        cursor = self.TextEdit.textCursor()
        line = cursor.blockNumber() + 1
        column = cursor.columnNumber() + 1
        position = cursor.position()
        self.statusBar.showMessage(f"Строка: {line} | Столбец: {column} | Позиция: {position}")

    def show_msg(self, msg: str) -> None:
        self.msg_box.setText(msg)
        self.msg_box.exec()

    @staticmethod
    def block_signals(objects: QtWidgets, block: bool) -> None:
        for obj in objects:
            obj.blockSignals(block)

    # обновление выделенной области
    def update_selection(self):
        self.block_signals(self.format_actions, True)
        self.font_combobox.setCurrentFont(self.TextEdit.currentFont())
        self.font_size_combobox.setCurrentText(str(int(self.TextEdit.fontPointSize())))
        self.italic_action.setChecked(self.TextEdit.fontItalic())
        self.under_line_action.setChecked(self.TextEdit.fontUnderline())
        self.bold_action.setChecked(self.TextEdit.fontWeight() == QtGui.QFont.Bold)

        self.left_alignment_action.setChecked(
            self.TextEdit.alignment().__index__() == QtCore.Qt.AlignmentFlag.AlignLeft.__index__())
        self.right_alignment_action.setChecked(
            self.TextEdit.alignment().__index__() == QtCore.Qt.AlignmentFlag.AlignRight.__index__())
        self.center_alignment_action.setChecked(
            self.TextEdit.alignment().__index__() == QtCore.Qt.AlignmentFlag.AlignCenter.__index__())
        self.justify_alignment_action.setChecked(
            self.TextEdit.alignment().__index__() == QtCore.Qt.AlignmentFlag.AlignJustify.__index__())

        for k, v in self.colors.items():
            if v == self.TextEdit.textColor().name():
                self.text_color_combobox.setCurrentText(k)
        cursor = self.TextEdit.textCursor()
        if not cursor.currentList():
            self.bullet_list_action.setChecked(False)
            self.numbered_list_action.setChecked(False)
        self.block_signals(self.format_actions, False)

    def set_font(self, font: QtGui.QFont) -> None:
        self.TextEdit.setCurrentFont(font)
        self.TextEdit.setFocus()

    def set_font_size(self, size: str) -> None:
        self.TextEdit.setFontPointSize(float(size))
        self.TextEdit.setFocus()

    def paint_text(self, color: str) -> None:
        self.TextEdit.setTextColor(QtGui.QColor(color))
        self.TextEdit.setFocus()

    def paint_back(self, color: str) -> None:
        self.TextEdit.setTextBackgroundColor(QtGui.QColor(color))
        self.TextEdit.setFocus()

    def open_file(self) -> None:
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                             caption=u'Открыть файл',
                                                             directory='E:/',
                                                             filter='HTML documents (*.html);')
        if file_path:
            try:
                with codecs.open(filename=file_path, mode="r", encoding="utf-8", errors="ignore") as file:
                    data = file.read()
            except Exception as e:
                self.show_msg("Не удалось открыть файл:\n" + str(e))
            else:
                self.selected_file = file_path
                self.TextEdit.setText(data)
                self.set_win_title()

    def save_file(self):
        if self.selected_file is None:
            return self.save_as_file()
        text = self.TextEdit.toHtml() if splitext(self.selected_file)[
                                             1] in self.html_extensions else self.TextEdit.toPlainText()
        try:
            with open(file=self.selected_file, mode='w', encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            self.show_msg("Не удалось сохранить файл:\n" + str(e))

    def save_as_file(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "",
                                                             "HTML documents (*.html)")
        if not file_path:
            return
        text = self.TextEdit.toHtml() if splitext(file_path)[
                                             1] in self.html_extensions else self.TextEdit.toPlainText()

        try:
            with open(file=file_path, mode='w', encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            self.show_msg("Не удалось сохранить файл:\n" + str(e))
        else:
            self.selected_file = file_path
            self.set_win_title()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = TextEditor()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
