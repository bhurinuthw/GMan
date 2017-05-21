from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from EditProfileStudent import editProfileUI

class profileUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Profile")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/background.png")))
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/bar.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/profile.ui",None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.grade_button = form.findChild(QPushButton,"gradeButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.temp = form.findChild(QPushButton, "temp")

        #page properties
        self.home_button = form.findChild(QPushButton, "homeButton")
        self.edit_button = form.findChild(QPushButton, "editButton")
        self.status = form.findChild(QLabel,"status")
        self.id = form.findChild(QLabel,"id")
        self.name = form.findChild(QLabel,"name")
        self.surname = form.findChild(QLabel,"surname")
        self.email = form.findChild(QLabel,"email")
        self.faculty = form.findChild(QLabel,"faculty")
        self.major = form.findChild(QLabel,"major")
        self.year = form.findChild(QLabel,"year")
        self.student_status = form.findChild(QLabel,"sstatus")
        self.address = form.findChild(QLabel,"address")

        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.course_button.clicked.connect(self.goCourse)
        self.temp.clicked.connect(self.goTemp)
        self.home_button.clicked.connect(self.goHome)
        self.edit_button.clicked.connect(self.editProfile)

    def goHome(self):
        self.parent.changePageLoginSection("home")

    def goProfile(self):
        self.parent.changePageLoginSection("profile")

    def goGrade(self):
        self.parent.changePageLoginSection("grade")

    def goCourse(self):
        self.parent.changePageLoginSection("course")

    def goTemp(self):
        self.parent.changePageLoginSection("addcourse")

    def editProfile(self):
        self.edit = editProfileUI()
        self.edit.show()
        
    

    def updatePage(self):
        data = self.parent.getCurrentUser()
        self.id.setText(data.getID())
        self.name.setText(data.getName())
        self.surname.setText(data.getSurname())
        self.email.setText(data.getEmail())
        self.faculty.setText(data.getFacultyName())
        self.major.setText(data.getMajorName())
        self.year.setText(data.year)
        self.address.setText(data.getAddress())

        #Status
        status = data.getStatus()
        if(status == 0):
            self.student_status.setText("Learning")
        elif(status==1):
            self.student_status.setText("Probation")
        elif (status == 2):
            self.student_status.setText("Retired")
        elif (status == 3):
            self.student_status.setText("Withdrawn")
        elif (status == 4):
            self.student_status.setText("Suspended")
        else:
            self.student_status.setText("Unknown")
