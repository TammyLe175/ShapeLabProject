# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
'''
this is view window file
'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AnswerButton = QtWidgets.QPushButton(self.centralwidget)
        self.AnswerButton.setGeometry(QtCore.QRect(80, 460, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AnswerButton.setFont(font)
        self.AnswerButton.setObjectName("AnswerButton")
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(159, 9, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.ShapeLabel = QtWidgets.QLabel(self.centralwidget)
        self.ShapeLabel.setGeometry(QtCore.QRect(10, 50, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ShapeLabel.setFont(font)
        self.ShapeLabel.setObjectName("ShapeLabel")
        self.CircleButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CircleButton.setGeometry(QtCore.QRect(90, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CircleButton.setFont(font)
        self.CircleButton.setObjectName("CircleButton")
        self.TriangleButton = QtWidgets.QRadioButton(self.centralwidget)
        self.TriangleButton.setGeometry(QtCore.QRect(230, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TriangleButton.setFont(font)
        self.TriangleButton.setObjectName("TriangleButton")
        self.SquareButton = QtWidgets.QRadioButton(self.centralwidget)
        self.SquareButton.setGeometry(QtCore.QRect(410, 50, 97, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.SquareButton.setFont(font)
        self.SquareButton.setObjectName("SquareButton")
        self.RectangleButton = QtWidgets.QRadioButton(self.centralwidget)
        self.RectangleButton.setGeometry(QtCore.QRect(90, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.RectangleButton.setFont(font)
        self.RectangleButton.setObjectName("RectangleButton")
        self.ParalButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ParalButton.setGeometry(QtCore.QRect(230, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ParalButton.setFont(font)
        self.ParalButton.setObjectName("ParalButton")
        self.RhombusButton = QtWidgets.QRadioButton(self.centralwidget)
        self.RhombusButton.setGeometry(QtCore.QRect(410, 90, 97, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.RhombusButton.setFont(font)
        self.RhombusButton.setObjectName("RhombusButton")
        self.RadiusLine = QtWidgets.QLineEdit(self.centralwidget)
        self.RadiusLine.setGeometry(QtCore.QRect(80, 130, 151, 22))
        self.RadiusLine.setObjectName("RadiusLine")
        self.RadiusLabel = QtWidgets.QLabel(self.centralwidget)
        self.RadiusLabel.setGeometry(QtCore.QRect(10, 130, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RadiusLabel.setFont(font)
        self.RadiusLabel.setObjectName("RadiusLabel")
        self.SideLabel = QtWidgets.QLabel(self.centralwidget)
        self.SideLabel.setGeometry(QtCore.QRect(260, 130, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SideLabel.setFont(font)
        self.SideLabel.setObjectName("SideLabel")
        self.SideLine = QtWidgets.QLineEdit(self.centralwidget)
        self.SideLine.setGeometry(QtCore.QRect(360, 130, 171, 22))
        self.SideLine.setObjectName("SideLine")
        self.LengthLabel = QtWidgets.QLabel(self.centralwidget)
        self.LengthLabel.setGeometry(QtCore.QRect(10, 175, 60, 21))
        self.LengthLabel.setObjectName("LengthLabel")
        self.LengthLine = QtWidgets.QLineEdit(self.centralwidget)
        self.LengthLine.setGeometry(QtCore.QRect(80, 170, 151, 22))
        self.LengthLine.setObjectName("LengthLine")
        self.WidthLabel = QtWidgets.QLabel(self.centralwidget)
        self.WidthLabel.setGeometry(QtCore.QRect(260, 170, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WidthLabel.setFont(font)
        self.WidthLabel.setObjectName("WidthLabel")
        self.WidthLine = QtWidgets.QLineEdit(self.centralwidget)
        self.WidthLine.setGeometry(QtCore.QRect(360, 170, 171, 22))
        self.WidthLine.setObjectName("WidthLine")
        self.BaseLabel = QtWidgets.QLabel(self.centralwidget)
        self.BaseLabel.setGeometry(QtCore.QRect(10, 220, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BaseLabel.setFont(font)
        self.BaseLabel.setObjectName("BaseLabel")
        self.BaseLine = QtWidgets.QLineEdit(self.centralwidget)
        self.BaseLine.setGeometry(QtCore.QRect(80, 220, 151, 22))
        self.BaseLine.setObjectName("BaseLine")
        self.HeightLabel = QtWidgets.QLabel(self.centralwidget)
        self.HeightLabel.setGeometry(QtCore.QRect(260, 220, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HeightLabel.setFont(font)
        self.HeightLabel.setObjectName("HeightLabel")
        self.HeightLine = QtWidgets.QLineEdit(self.centralwidget)
        self.HeightLine.setGeometry(QtCore.QRect(360, 220, 171, 22))
        self.HeightLine.setObjectName("HeightLine")
        self.AnswerLine = QtWidgets.QTextEdit(self.centralwidget)
        self.AnswerLine.setGeometry(QtCore.QRect(20, 270, 241, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AnswerLine.setFont(font)
        self.AnswerLine.setObjectName("AnswerLine")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(310, 460, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.ClearButton.setFont(font)
        self.ClearButton.setObjectName("ClearButton")
        self.ImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageLabel.setGeometry(QtCore.QRect(290, 270, 261, 161))
        self.ImageLabel.setText("")
        self.ImageLabel.setPixmap(QtGui.QPixmap("../../Library/CloudStorage/OneDrive-UniversityofNebraskaatOmaha/IT Ethics/shapeimage.png"))
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 574, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AnswerButton.setText(_translate("MainWindow", "Answer"))
        self.TitleLabel.setText(_translate("MainWindow", "Geometry Calculator"))
        self.ShapeLabel.setText(_translate("MainWindow", "Shape"))
        self.CircleButton.setText(_translate("MainWindow", "Circle"))
        self.TriangleButton.setText(_translate("MainWindow", "Right Triangle"))
        self.SquareButton.setText(_translate("MainWindow", "Square"))
        self.RectangleButton.setText(_translate("MainWindow", "Rectangle "))
        self.ParalButton.setText(_translate("MainWindow", "Parallelogram"))
        self.RhombusButton.setText(_translate("MainWindow", "Rhombus"))
        self.RadiusLabel.setText(_translate("MainWindow", "Radius "))
        self.SideLabel.setText(_translate("MainWindow", "Side(a)"))
        self.LengthLabel.setText(_translate("MainWindow", "Length"))
        self.WidthLabel.setText(_translate("MainWindow", "Width"))
        self.BaseLabel.setText(_translate("MainWindow", "Base(b)"))
        self.HeightLabel.setText(_translate("MainWindow", "Height(h)"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
