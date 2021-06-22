import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import email.encoders as encoders
from PyQt5 import QtWidgets, QtCore
import MailInterface
import sys
import os
import mimetypes

class MailAPP(QtWidgets.QMainWindow, QtWidgets.QFileDialog, MailInterface.Ui_ProjectWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Почта')
        self.setFocus()
        self.FilesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.myEMAIL = ''
        self.myPassword = ''
        self.PasswordEnter.setEchoMode(QtWidgets.QLineEdit.Password)
        services = ['gmail.com', 'mail.ru', 'yandex.ru']
        self.servers = {'gmail.com': 'smtp.gmail.com:587',
                        'mail.ru': 'smtp.yandex.ru:467',
                        'yandex.ru': 'smtp.mail.ru:25'}
        # выбор сервера
        for service in services:
            self.ServerComboBox.addItem(service)
        self.SendButton.clicked.connect(self.sendMail)              # привязка кпоки "Отправить" к функции sendMail
        self.AddFilePushButton.clicked.connect(self.addFile)        # привязка кпоки "Выбрать файл" к функции addFile
        self.DeleteFilePushButton.clicked.connect(self.rmvFiles)    # привязка кпоки "Удалить файлы" к функции rmvFiles
        self.msgBox = QtWidgets.QMessageBox()

    # реализация функции диалогового окна
    def showMsgBox(self, msg: str):
        self.msgBox.setText(msg)
        self.msgBox.exec_()

    # реализация функции добавить файл
    def addFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                         caption=u'Открыть файл',
                                                         directory='E:/',
                                                         filter='AllFiles (*)')[0]
        if fileName:  # Если выбран файл
            # Проверка на наличие одинаковых файлов
            if len(self.FilesListWidget.findItems(fileName, QtCore.Qt.MatchExactly)) == 0:
                self.FilesListWidget.addItem(fileName)
            else:
                self.showMsgBox('Файл уже добавлен!')

    # реализация функции удалить файл
    def rmvFiles(self):
        for item in self.FilesListWidget.selectedItems():
            self.FilesListWidget.takeItem(self.FilesListWidget.row(item))

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
                self.showMsgBox('Возникла ошибка при отправке файла: ' + fileName)
        return filesList

    # реализация функции отправить сообщение
    def sendMail(self):
        try:
            print()
            if self.LoginEnter.text().split('@')[1] != self.ServerComboBox.currentText():
                self.showMsgBox('Введенная почта и сервер не совпадают!')
            else:
                self.smtpServer = smtplib.SMTP(self.servers[self.ServerComboBox.currentText()])  # Создание объекта SMTP
                self.myEMAIL = self.LoginEnter.text()
                self.myPassword = self.PasswordEnter.text()
                self.smtpServer.starttls()  # Шифрование
                self.smtpServer.login(self.myEMAIL, self.myPassword)  # Ввод учетных данных

                myMessage = MIMEMultipart()  # Создание объекта стандарта MIME
                myMessage['Subject'] = self.ThemeBar.text()  # Определение темы сообщения
                myMessage['From'] = self.myEMAIL  # Определение почты отправки
                myMessage['To'] = self.AddressLineEdit.text()  # Определение адресата
                messageContent = self.textEdit.toPlainText()  # Получение текста с формы
                myMessage.attach(MIMEText(messageContent, 'plain'))  # Добавление текста в сообещение

                for file in self.processAttachment():
                    myMessage.attach(file)
                self.smtpServer.send_message(myMessage)  # Отправка сообщения
        except:
            self.showMsgBox('Возникла не предвиденная ошибка')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MailAPP()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
