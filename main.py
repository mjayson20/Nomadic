from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys
import source
import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'AdminMJ', passwd = 'doodle123mj', database = 'nomadic')
if mycon.is_connected():
    print("Success")

class front(QtWidgets.QMainWindow):
    def __init__(self):
        super(front, self).__init__()
        loadUi("front.ui", self)
        self.pushButton1.clicked.connect(self.gotosignup)
        self.pushButton.clicked.connect(self.gotouserd)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        


    def gotosignup(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    def gotouserd(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

class signup(QtWidgets.QMainWindow):
    def __init__(self):
        super(signup, self).__init__()
        loadUi("signup.ui", self)
        self.gobackbutton.clicked.connect(self.gotofront)
        self.signupbutton.clicked.connect(self.gotofront)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def gotofront(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class userdash(QtWidgets.QMainWindow):
    def __init__(self):
        super(userdash, self).__init__()
        loadUi("userdash.ui", self)
        

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
screen01 = front()
screen02 = signup()
screen03 = userdash()
widget.addWidget(screen01)
widget.addWidget(screen02)
widget.addWidget(screen03)
widget.setFixedHeight(700)
widget.setFixedWidth(980)
widget.setWindowTitle('Nomadic')
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exited")
