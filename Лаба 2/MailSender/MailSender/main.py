import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import email.encoders as encoders
# import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
import MailInterface
import sys
import os
import mimetypes

class MailAPP(QtWidgets.QMainWindow, QtWidgets.QFileDialog, MailInterface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Почта')
        self.setFocus()
        self.FilesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.myEMAIL = ''
        self.myPassword = ''
        self.PasswordEnter.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.contacts = ['uncledeni@mail.ru', 'uncledeni@yandex.ru']
        services = ['gmail.com', 'mail.ru', 'yandex.ru']
        self.servers = {'gmail.com': 'smtp.gmail.com:587',
                        'mail.ru': 'smtp.yandex.ru:467',
                        'yandex.ru': 'smtp.mail.ru:25'}
        for service in services:
            self.ServerComboBox.addItem(service)
        self.SendButton.clicked.connect(self.sendMail)  # self.sendMail
        self.AddFilePushButton.clicked.connect(self.addFile)
        self.DeleteFilePushButton.clicked.connect(self.rmvFiles)
        self.msgBox = QtWidgets.QMessageBox()


    def showMsgBox(self, msg: str):
        self.msgBox.setText(msg)
        self.msgBox.exec_()

    # Функция добавления нового файла
    def addFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                         caption=u'Открыть файл',
                                                         directory='E:/',
                                                         filter='AllFiles (*)')[0]

        # Проверка на наличие дубликатов
        if fileName:
            if len(self.FilesListWidget.findItems(fileName, QtCore.Qt.MatchExactly)) == 0:
                self.FilesListWidget.addItem(fileName)
            else:
                self.showMsgBox('Данный файл уже добавлен')


    def rmvFiles(self):
        for item in self.FilesListWidget.selectedItems():
            self.FilesListWidget.takeItem(self.FilesListWidget.row(item))


    # Формирование списка файлов
    def processAttachment(self):
        filesList = []
        for i in range(self.FilesListWidget.count()):
            fileName = ''
            try:
                item = self.FilesListWidget.item(i).text()
                fileName = os.path.basename(item)
                ctype, encoding = mimetypes.guess_type(item)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                if maintype == 'text':
                    with open(item) as fp:
                        file = MIMEText(fp.read(), _subtype=subtype)
                        fp.close()
                elif maintype == 'image':
                    with open(item, 'rb') as fp:
                        file = MIMEImage(fp.read(), _subtype=subtype)
                        fp.close()
                elif maintype == 'audio':
                    with open(item, 'rb') as fp:
                        file = MIMEAudio(fp.read(), _subtype=subtype)
                        fp.close()
                else:
                    with open(item, 'rb') as fp:
                        file = MIMEBase(maintype, subtype)
                        file.set_payload(fp.read())
                        fp.close()
                        encoders.encode_base64(file)
                file.add_header('Content-Disposition', 'attachment', filename=fileName)
                filesList.append(file)
            except:
                self.showMsgBox('Ошибка отправка файла: ' + fileName)
        return filesList

    # Отправка письма
    def sendMail(self):
        try:
            print()
            if self.LoginEnter.text().split('@')[1] != self.ServerComboBox.currentText():
                self.showMsgBox('Введенная почта и сервер не совпадают!')
            else:
                self.smtpServer = smtplib.SMTP(self.servers[self.ServerComboBox.currentText()])  # Создание объекта SMTP
                self.myEMAIL = self.SenderLineEdit.text()
                self.myPassword = self.PasswordLineEdit.text()
                self.smtpServer.starttls()  # Шифрование
                self.smtpServer.login(self.myEMAIL, self.myPassword)  # Ввод учетных данных
                myMessage = MIMEMultipart()  # Создание объекта стандарта MIME
                myMessage['Subject'] = self.ThemeBar.text()  # Тема сообщения
                myMessage['From'] = self.myEMAIL  # Отправитель
                myMessage['To'] = self.PersonComboBox.currentText()  # Получатель
                messageContent = self.textEdit.toPlainText()  # Получение текста с формы
                myMessage.attach(MIMEText(messageContent, 'plain'))  # Добавление текста в сообещение
                for file in self.processAttachment():
                    myMessage.attach(file)
                self.smtpServer.send_message(myMessage)  # Отправка сообщения
        except:
            self.showMsgBox('Произошёл сбой')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MailAPP()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
