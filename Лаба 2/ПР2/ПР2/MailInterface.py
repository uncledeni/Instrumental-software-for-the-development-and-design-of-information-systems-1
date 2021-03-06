# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mailSenderUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProjectWindow(object):
    def setupUi(self, ProjectWindow):
        ProjectWindow.setObjectName("ProjectWindow")
        ProjectWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ProjectWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # первый горизонтальный блок
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_1.addWidget(self.label_1)
        # добавление выпадающего списка серверов
        self.ServerComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ServerComboBox.setObjectName("ServerComboBox")
        self.horizontalLayout_1.addWidget(self.ServerComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_1)

        # второй горизонтальный блок
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        # добавление поля логина
        self.LoginEnter = QtWidgets.QLineEdit(self.centralwidget)
        self.LoginEnter.setObjectName("LoginEnter")
        self.horizontalLayout_2.addWidget(self.LoginEnter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        # третий горизонтальный блок
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        # добавление пустого разделяющего пространства
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        # добавление поля пароля
        self.PasswordEnter = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEnter.setObjectName("PasswordEnter")
        self.horizontalLayout_3.addWidget(self.PasswordEnter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)

        # четвёртый горизонтальный блок
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        # формирование кнопки "Добавить файл"
        self.AddFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddFilePushButton.setObjectName("AddFilePushButton")
        self.horizontalLayout_4.addWidget(self.AddFilePushButton)
        # формирование кнопки "Удалить файл"
        self.DeleteFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteFilePushButton.setObjectName("DeleteFilePushButton_2")
        self.horizontalLayout_4.addWidget(self.DeleteFilePushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        # формирование списка добавленных файлов
        self.FilesListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.FilesListWidget.setObjectName("FilesListWidget")
        self.verticalLayout_2.addWidget(self.FilesListWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        # пятый горизонтальный блок
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        # добавление поля адресата
        self.AddressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddressLineEdit.setObjectName("AddressLineEdit")
        self.horizontalLayout_5.addWidget(self.AddressLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        # шестой горизонтальный блок
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        # добавление поля для темы
        self.ThemeBar = QtWidgets.QLineEdit(self.centralwidget)
        self.ThemeBar.setObjectName("ThemeBar")
        self.horizontalLayout_6.addWidget(self.ThemeBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout")
        # добавление поля сообщения
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_1.addWidget(self.textEdit)
        # добавление кнопки отправки
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setObjectName("SendButton")
        self.verticalLayout_1.addWidget(self.SendButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_1)
        ProjectWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(ProjectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        ProjectWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(ProjectWindow)
        self.statusbar.setObjectName("statusbar")
        ProjectWindow.setStatusBar(self.statusbar)

        self.namingInUi(ProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(ProjectWindow)


    def namingInUi(self, ProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        ProjectWindow.setWindowTitle(_translate("ProjectWindow", "ProjectWindow"))

        self.label_1.setText(_translate("ProjectWindow", "Сервер"))
        self.label_2.setText(_translate("ProjectWindow", "Адрес Отправителя"))
        self.label_3.setText(_translate("ProjectWindow", "Пароль"))
        self.label_4.setText(_translate("ProjectWindow", "Список файлов"))

        self.AddFilePushButton.setText(_translate("ProjectWindow", "Выбрать файл"))
        self.DeleteFilePushButton.setText(_translate("ProjectWindow", "Удалить файлы"))

        self.label_5.setText(_translate("ProjectWindow", "Адрес получателя"))
        self.label_6.setText(_translate("ProjectWindow", "Тема"))

        self.SendButton.setText(_translate("ProjectWindow", "Отправить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProjectWindow = QtWidgets.QMainWindow()
    ui = Ui_ProjectWindow()
    ui.setupUi(ProjectWindow)
    ProjectWindow.show()
    sys.exit(app.exec_())
