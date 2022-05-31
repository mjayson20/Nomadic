from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import sys
import source, source02, discover, trending
import mysql.connector as mys


class front(QtWidgets.QMainWindow):
    def __init__(self):
        super(front, self).__init__()
        loadUi("front.ui", self)
        self.pushButton1.clicked.connect(self.gotosignup)
        self.profilecomb.activated[str].connect(self.onActivated)

        
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def onActivated(self):
        profile = self.profilecomb.currentText()
        if (profile == 'User') :
             self.pushButton.clicked.connect(self.gotouserd)
        elif (profile == 'Nomadic'):
            self.pushButton.clicked.connect(self.gotonomad)  
        elif (profile == 'Admin'):
            print("Admin Soon")


    
    def gotosignup(self):
        widget.setCurrentIndex(1)   
    def gotouserd(self):
        msg = QtWidgets.QMessageBox()
        if (self.usernameEdit.text() == 'xxx' and self.passwordEdit.text() == '000'):
            msg.setText('Success')
            msg.setWindowTitle('Login')
            msg.setWindowIcon(QtGui.QIcon("iconpg.png"))
            msg.setFixedWidth(500)
            msg.setFixedHeight(400)
            msg.exec_()
            widget.setCurrentIndex(2)
        else:
            msg.setText('Invalid Credentials')
            msg.setWindowTitle('Login')
            msg.setWindowIcon(QtGui.QIcon("iconpg.png"))
            msg.setFixedWidth(500)
            msg.setFixedHeight(400)
            msg.exec_()
        
    def gotonomad(self):
        msg = QtWidgets.QMessageBox()
        if (self.usernameEdit.text() == 'xxx' and self.passwordEdit.text() == '000'):
            msg.setText('Success')
            msg.setWindowTitle('Login')
            msg.setWindowIcon(QtGui.QIcon("iconpg.png"))
            msg.setFixedWidth(500)
            msg.setFixedHeight(400)
            msg.exec_()
            widget.setCurrentIndex(3)
        else:
            msg.setText('Invalid Credentials')
            msg.setWindowTitle('Login')
            msg.setWindowIcon(QtGui.QIcon("iconpg.png"))
            msg.setFixedWidth(500)
            msg.setFixedHeight(400)
            msg.exec_()

#dashboardbuttons
class home(QtWidgets.QMainWindow):
    def __init__(self):
        super(home, self).__init__()
        loadUi("userdash.ui", self)
        self.accGoback.clicked.connect(self.gotouserdash)
    def gotouserdash(self):
        widget.setCurrentIndex(2)

class discoverpg(QtWidgets.QMainWindow):
    def __init__(self):
        super(discoverpg, self).__init__()
        loadUi("discover.ui", self)
        self.accGoback.clicked.connect(self.gotouserdash)
    def gotouserdash(self):
        widget.setCurrentIndex(2)

class trendingpg(QtWidgets.QMainWindow):
    def __init__(self):
        super(trendingpg, self).__init__()
        loadUi("trending.ui", self)
        self.accGoback.clicked.connect(self.gotouserdash)
    def gotouserdash(self):
        widget.setCurrentIndex(2)

class yourtravels(QtWidgets.QMainWindow):
    def __init__(self):
        super(yourtravels, self).__init__()
        loadUi("travelhistory.ui", self)
        self.accGoback.clicked.connect(self.gotouserdash)
    def gotouserdash(self):
        widget.setCurrentIndex(2)

class account(QtWidgets.QMainWindow):
    def __init__(self):
        super(account, self).__init__()
        loadUi("account.ui", self)
        self.accGoback.clicked.connect(self.gotouserdash)
    def gotouserdash(self):
        widget.setCurrentIndex(2)

class cred(QtWidgets.QMainWindow):
    def __init__(self):
        super(cred, self).__init__()
        loadUi("creds.ui", self)
        self.accGoback.clicked.connect(self.gotouserdash)
    def gotouserdash(self):
        widget.setCurrentIndex(2)



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

        self.discoverpush.clicked.connect(self.gotodiscover)
        self.trendingpush.clicked.connect(self.gototrending)
        self.travelspush.clicked.connect(self.gototravels)
        self.accountpush.clicked.connect(self.gotoaccount)
        self.logoutPush.clicked.connect(self.backtofront)
    
   
    def gotodiscover(self):
        widget.setCurrentIndex(4)
    def gototrending(self):
        widget.setCurrentIndex(5)
    def gototravels(self):
        widget.setCurrentIndex(6)
    def gotoaccount(self):
        widget.setCurrentIndex(7)
    def backtofront(self):
        widget.setCurrentIndex(0)

        
class nomaddash(QtWidgets.QMainWindow):
    def __init__(self):
        super(nomaddash, self).__init__()
        loadUi("nomaddash.ui", self)
        self.discoverPush.clicked.connect(self.gotodiscover)
        self.trendingPush.clicked.connect(self.gototrending)
        self.travelsPush.clicked.connect(self.gototravels)
        self.accPush.clicked.connect(self.gotoaccount)
        self.credPush.clicked.connect(self.gotocred)
        self.logoutPush.clicked.connect(self.backtofront)
       
        
    def gotodiscover(self):
        widget.setCurrentIndex(4)
    def gototrending(self):
        widget.setCurrentIndex(5)
    def gototravels(self):
        widget.setCurrentIndex(6)
    def gotoaccount(self):
        widget.setCurrentIndex(7)
    def gotocred(self):
        widget.setCurrentIndex(8)
    def backtofront(self):
        widget.setCurrentIndex(0)

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
screen00 = front()
screen01 = signup()
screen02 = userdash()
screen03 = nomaddash()
screen04 = discoverpg()
screen05 = trendingpg()
screen06 = yourtravels()
screen07 = account()
screen08 = cred()
widget.addWidget(screen00)
widget.addWidget(screen01)
widget.addWidget(screen02)
widget.addWidget(screen03)
widget.addWidget(screen04)
widget.addWidget(screen05)
widget.addWidget(screen06)
widget.addWidget(screen07)
widget.addWidget(screen08)
widget.setWindowIcon(QtGui.QIcon("iconpg.png"))
widget.setFixedSize(1024, 768)
widget.setWindowTitle('Nomadic')
widget.show()

sys.exit(app.exec_())
