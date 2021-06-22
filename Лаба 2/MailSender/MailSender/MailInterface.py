# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mail.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_1)

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
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        # третий горизонтальный блок
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        # добавление поля пароля
        self.PasswordEnter = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEnter.setObjectName("PasswordEnter")
        self.horizontalLayout_3.addWidget(self.PasswordEnter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        # шестой горизонтальный блок
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        # добавление выпадающего списка почт
        self.PersonComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.PersonComboBox.setObjectName("PersonComboBox")
        self.horizontalLayout_6.addWidget(self.PersonComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        # седьмой горизонтальный блок
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        # добавление поля для темы
        self.ThemeBar = QtWidgets.QLineEdit(self.centralwidget)
        self.ThemeBar.setObjectName("ThemeBar")
        self.horizontalLayout_7.addWidget(self.ThemeBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_1.addWidget(self.textEdit)
        # добавление кнопки отправки
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setObjectName("SendButton")
        self.verticalLayout_1.addWidget(self.SendButton)

        self.verticalLayout_2.addLayout(self.verticalLayout_1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        ProjectWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(ProjectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 277, 21))
        self.menubar.setObjectName("menubar")
        ProjectWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(ProjectWindow)
        self.statusbar.setObjectName("statusbar")
        ProjectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(ProjectWindow)

    def retranslateUi(self, ProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        ProjectWindow.setWindowTitle(_translate("ProjectWindow", "ProjectWindow"))
        self.label_1.setText(_translate("ProjectWindow", "Сервер"))
        self.label_2.setText(_translate("ProjectWindow", "Адрес отправителя"))
        self.label_3.setText(_translate("ProjectWindow", "Пароль"))
        self.label_6.setText(_translate("ProjectWindow", "Адрес получателя"))
        self.label_7.setText(_translate("ProjectWindow", "Тема"))
        self.SendButton.setText(_translate("ProjectWindow", "Отправить"))

