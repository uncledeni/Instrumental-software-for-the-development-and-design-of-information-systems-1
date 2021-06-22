import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
import MailInterface
import sys

class MailAPP(QtWidgets.QMainWindow, MailInterface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.myEMAIL = 'uncledeni98@gmail.com'
        self.myPassword = 'BDA36robola'

        self.smtpServer = smtplib.SMTP('smtp.gmail.com:587')
        self.smtpServer.starttls()
        self.smtpServer.login(self.myEMAIL, self.myPassword)
        self.contacts = ['uncledeni@mail.ru']
        self.SendButton.clicked.connect(self.sendMail)
        for i in self.contacts:
            self.PersonComboBox.addItem(i)

    def sendMail(self):
        myMessage = MIMEMultipart()
        myMessage['Subject'] = self.ThemeBar.text()
        myMessage['From'] = self.myEMAIL
        myMessage['To'] = self.PersonComboBox.currentText()
        messageContent = self.textEdit.toPlainText()
        myMessage.attach(MIMEText(messageContent, 'plain'))
        self.smtpServer.send_message(myMessage)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MailAPP()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
