import sys
import bcrypt
from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi

import source, source02, discover, trending
from db import get_connection, init_db

# ---------------------------------------------------------------------------
# Session — tracks the currently logged-in user across all screens
# ---------------------------------------------------------------------------
class Session:
    username: str = ""
    role: str = ""          # 'User' or 'Nomadic'

    @classmethod
    def set(cls, username: str, role: str):
        cls.username = username
        cls.role = role

    @classmethod
    def clear(cls):
        cls.username = ""
        cls.role = ""

    @classmethod
    def home_index(cls) -> int:
        """Return the QStackedWidget index for the current user's dashboard."""
        return 2 if cls.role == "User" else 3


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _msg_box(title: str, text: str) -> QtWidgets.QMessageBox:
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setWindowIcon(QtGui.QIcon("iconpg.png"))
    return msg


def _verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())


def _hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()


def _db_login(username: str, password: str, expected_role: str):
    """
    Returns (success: bool, message: str).
    Checks username, bcrypt password, and role against the DB.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT password, role FROM users WHERE username = %s",
            (username,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        return False, f"Database error: {e}"

    if not row:
        return False, "Invalid credentials."
    if not _verify_password(password, row["password"]):
        return False, "Invalid credentials."
    if row["role"] != expected_role:
        return False, f"This account is not registered as '{expected_role}'."

    return True, "Success"


def _db_register(username: str, password: str, role: str):
    """
    Returns (success: bool, message: str).
    Inserts a new user with a bcrypt-hashed password.
    """
    if not username or not password:
        return False, "Username and password cannot be empty."

    hashed = _hash_password(password)
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
            (username, hashed, role)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        # Duplicate username raises IntegrityError
        if "Duplicate entry" in str(e):
            return False, "Username already taken."
        return False, f"Database error: {e}"

    return True, "Account created successfully."


# ---------------------------------------------------------------------------
# Screens
# ---------------------------------------------------------------------------
class front(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("front.ui", self)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton1.clicked.connect(self.gotosignup)
        self.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.usernameEdit.text().strip()
        password = self.passwordEdit.text()
        role = self.profilecomb.currentText()

        if role == "Admin":
            _msg_box("Login", "Admin login is not yet available.").exec_()
            return

        if role not in ("User", "Nomadic"):
            _msg_box("Login", "Please select a profile type.").exec_()
            return

        ok, message = _db_login(username, password, role)
        if ok:
            Session.set(username, role)
            _msg_box("Login", f"Welcome, {username}!").exec_()
            widget.setCurrentIndex(Session.home_index())
            # Clear fields after successful login
            self.usernameEdit.clear()
            self.passwordEdit.clear()
        else:
            _msg_box("Login", message).exec_()

    def gotosignup(self):
        widget.setCurrentIndex(1)


class signup(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("signup.ui", self)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gobackbutton.clicked.connect(self.backtofront)
        self.signupbutton.clicked.connect(self.handle_signup)

    def handle_signup(self):
        # Assumes the signup form has: usernameEdit, lineEdit (pw), lineEdit_2 (confirm pw), rolecomb
        username = self.usernameEdit.text().strip() if hasattr(self, "usernameEdit") else ""
        password = self.lineEdit.text()
        confirm  = self.lineEdit_2.text()
        role     = self.rolecomb.currentText() if hasattr(self, "rolecomb") else "User"

        if password != confirm:
            _msg_box("Sign Up", "Passwords do not match.").exec_()
            return

        if len(password) < 6:
            _msg_box("Sign Up", "Password must be at least 6 characters.").exec_()
            return

        ok, message = _db_register(username, password, role)
        _msg_box("Sign Up", message).exec_()
        if ok:
            self.backtofront()

    def backtofront(self):
        widget.setCurrentIndex(0)


class userdash(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("userdash.ui", self)
        self.discoverpush.clicked.connect(lambda: widget.setCurrentIndex(4))
        self.trendingpush.clicked.connect(lambda: widget.setCurrentIndex(5))
        self.travelspush.clicked.connect(lambda: widget.setCurrentIndex(6))
        self.accountpush.clicked.connect(lambda: widget.setCurrentIndex(7))
        self.logoutPush.clicked.connect(self.logout)

    def logout(self):
        Session.clear()
        widget.setCurrentIndex(0)


class nomaddash(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("nomaddash.ui", self)
        self.discoverPush.clicked.connect(lambda: widget.setCurrentIndex(4))
        self.trendingPush.clicked.connect(lambda: widget.setCurrentIndex(5))
        self.travelsPush.clicked.connect(lambda: widget.setCurrentIndex(6))
        self.accPush.clicked.connect(lambda: widget.setCurrentIndex(7))
        self.credPush.clicked.connect(lambda: widget.setCurrentIndex(8))
        self.logoutPush.clicked.connect(self.logout)

    def logout(self):
        Session.clear()
        widget.setCurrentIndex(0)


class discoverpg(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("discover.ui", self)
        self.accGoback.clicked.connect(lambda: widget.setCurrentIndex(Session.home_index()))


class trendingpg(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("trending.ui", self)
        self.accGoback.clicked.connect(lambda: widget.setCurrentIndex(Session.home_index()))


class yourtravels(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("travelhistory.ui", self)
        self.accGoback.clicked.connect(lambda: widget.setCurrentIndex(Session.home_index()))


class account(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("account.ui", self)
        self.accGoback.clicked.connect(lambda: widget.setCurrentIndex(Session.home_index()))


class cred(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("creds.ui", self)
        self.accGoback.clicked.connect(lambda: widget.setCurrentIndex(Session.home_index()))


# ---------------------------------------------------------------------------
# Bootstrap
# ---------------------------------------------------------------------------
init_db()   # Create tables if they don't exist yet

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

for screen in [screen00, screen01, screen02, screen03,
               screen04, screen05, screen06, screen07, screen08]:
    widget.addWidget(screen)

widget.setWindowIcon(QtGui.QIcon("iconpg.png"))
widget.setFixedSize(1024, 768)
widget.setWindowTitle("Nomadic")
widget.show()

sys.exit(app.exec_())
