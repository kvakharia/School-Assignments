###########IMPORT LIBRARIES################
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi 

####CREATING CLASS AND FUNCTIONS#################
class Login(QMainWindow): # Creating a class for the mainwindow
    def __init__(self):
        super(Login, self).__init__() # Initializing the class.

        loadUi("Login.ui", self) # Loading the UI

        self.login_btn.clicked.connect(self.login_function)

    def login_function(self):
        Username = self.Username.text() # Grabbing the text from the username field.
        Password = self.Password.text() # Grabbing the text from the password field.
        if Username == "user0" and Password == "test":
            print("The admin account, " + "'" + Username + "'" " has logged in with the password " + "'" + Password + "'" + ".")


#########INITIALIZING THE PROGRAM TO MAKE SURE IT OPENS AND CLOSES PROPERLY#################
app=QApplication(sys.argv)
LoginWindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(LoginWindow)
widget.setFixedWidth(540)
widget.setFixedHeight(514)
widget.show()
app.exec_()