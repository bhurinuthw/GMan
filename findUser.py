from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConn as database

class findUserUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(741,351)
        self.setWindowTitle("User_Information")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/FindUsers.ui",None)
        self.setCentralWidget(form)

        #QPushButton
        self.cancel_button = form.findChild(QPushButton,"pushButton_3")
        self.search_button = form.findChild(QPushButton,"pushButton")

        #LineEdit
        self.search_user_id = form.findChild(QLineEdit,"lineEdit")

        #Label
        self.user_id = form.findChild(QLabel,"label_16")
        self.user_name = form.findChild(QLabel, "label_20")
        self.first_name = form.findChild(QLabel,"label_17")
        self.surname = form.findChild(QLabel,"label_18")
        self.email = form.findChild(QLabel,"label_19")
        self.type = form.findChild(QLabel,"label_21")
        self.faculty_id = form.findChild(QLabel,"label_22")
        self.major_id = form.findChild(QLabel,"label_23")
    
        #Connect
        self.search_user_id.returnPressed.connect(self.search)
        self.cancel_button.clicked.connect(self.cancel)
        self.search_button.clicked.connect(self.search)

    def cancel(self):
        self.close()

    def search(self):
        db = database.databaseLogin()
        data = db.getInformationUser(self.search_user_id.text())
        if(data[0] is not None and data[1] is not None):
            self.user_id.setText(data[0].user_id)
            self.user_name.setText(data[0].username)
            self.first_name.setText(data[1].name)
            self.surname.setText(data[1].surname)
            self.email.setText(data[1].email)
            self.faculty_id.setText(str(data[1].facultyID))
            self.major_id.setText(str(data[1].majorID))
            status = int(data[0].user_type)
            if (status == 0):
                self.type.setText("STUDENT")
            elif (status == 1):
                self.type.setText("PROFESSOR")
            elif (status == 2):
                self.type.setText("ADMINISTRATOR")