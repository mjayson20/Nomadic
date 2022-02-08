from turtle import screensize
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
        widget.setCurrentIndex(1)   
    def gotouserd(self):
        widget.setCurrentIndex(2)


#dashboardbuttons
class home(QtWidgets.QMainWindow):
    def __init__(self):
        super(home, self).__init__()
        loadUi("userdash.ui", self)

class discover(QtWidgets.QMainWindow):
    def __init__(self):
        super(discover, self).__init__()
        loadUi("discover.ui", self)

class trending(QtWidgets.QMainWindow):
    def __init__(self):
        super(trending, self).__init__()
        loadUi("trending.ui", self)

class yourtravels(QtWidgets.QMainWindow):
    def __init__(self):
        super(yourtravels, self).__init__()
        loadUi("travelhistory.ui", self)

class account(QtWidgets.QMainWindow):
    def __init__(self):
        super(account, self).__init__()
        loadUi("account.ui", self)



class signup(QtWidgets.QMainWindow):
    def __init__(self):
        super(signup, self).__init__()
        loadUi("signup.ui", self)
        self.gobackbutton.clicked.connect(self.backtofront)
        self.signupbutton.clicked.connect(self.backtofront)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def backtofront(self):
        widget.setCurrentIndex(0)



class userdash(QtWidgets.QMainWindow):
    def __init__(self):
        super(userdash, self).__init__()
        loadUi("userdash.ui", self)
        self.homepush.clicked.connect(self.gotouserdash)
        self.discoverpush.clicked.connect(self.gotodiscover)
        self.trendingpush.clicked.connect(self.gototrending)
        self.travelspush.clicked.connect(self.gototravels)
        self.accountpush.clicked.connect(self.gotoaccount)
    
    def gotouserdash(self):
        widget.setCurrentIndex(4)
    def gotodiscover(self):
        widget.setCurrentIndex(5)
    def gototrending(self):
        widget.setCurrentIndex(6)
    def gototravels(self):
        widget.setCurrentIndex(7)
    def gotoaccount(self):
        widget.setCurrentIndex(8)
    

        
class nomaddash(QtWidgets.QMainWindow):
    def __init__(self):
        super(nomaddash, self).__init__()
        loadUi("nomaddash.ui", self)
        

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
screen00 = front()
screen01 = signup()
screen02 = userdash()
screen03 = nomaddash()
screen04 = home()
screen05 = discover()
screen06 = trending()
screen07 = yourtravels()
screen08 = account()
widget.addWidget(screen00)
widget.addWidget(screen01)
widget.addWidget(screen02)
widget.addWidget(screen03)
widget.addWidget(screen04)
widget.addWidget(screen05)
widget.addWidget(screen06)
widget.addWidget(screen07)
widget.addWidget(screen08)


widget.setWindowTitle('Nomadic')
widget.show()

sys.exit(app.exec_())

