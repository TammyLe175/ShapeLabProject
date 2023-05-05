from view import *
from PyQt5.QtWidgets import *
from math import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #add 6 radio button

        self.CircleButton.toggled.connect(self.Circle)
        self.SquareButton.toggled.connect(self.Square)


        #answer and clear button
        self.AnswerButton.clicked.connect(lambda: self.Submit())
        self.ClearButton.clicked.connect(lambda: self.Clear())

        # set all input box hidden
        self.RadiusLabel.setHidden(True)
        self.RadiusLine.setHidden(True)
        self.LengthLabel.setHidden(True)
        self.LengthLine.setHidden(True)
        self.BaseLabel.setHidden(True)
        self.BaseLine.setHidden(True)
        self.SideLabel.setHidden(True)
        self.SideLine.setHidden(True)
        self.WidthLabel.setHidden(True)
        self.WidthLine.setHidden(True)
        self.HeightLabel.setHidden(True)
        self.HeightLine.setHidden(True)
        self.AnswerLine.setHidden(True)

        #set all radio button in a group
        self.group_button = QButtonGroup(self)
        self.group_button.addButton(self.CircleButton)
        self.group_button.addButton(self.SquareButton)
        self.group_button.addButton(self.TriangleButton)
        self.group_button.addButton(self.RectangleButton)
        self.group_button.addButton(self.ParalButton)
        self.group_button.addButton(self.RhombusButton)

        #create variable
        self.circle_A = 0.00
        self.circle_P = 0.00
        self.square_A = 0.00
        self.square_P = 0.00

    def Circle(self):
        """
        calculate the area and perimeter of circle
        """
        self.RadiusLabel.setHidden(False)
        self.RadiusLine.setHidden(False)
        try:
            radius = float(self.RadiusLine.text())

        except ValueError:
            self.AnswerLine.setText("invalid")
            return
        self.circle_A = pi * radius ** 2
        self.circle_P = pi * 2 * radius
        self.AnswerLine.setText(f"Area = {self.circle_A} \n Perimeter = {self.circle_P}")


    def Square(self):
        '''
        calculate the area and perimeter of square
        '''
        self.SideLabel.setHidden(False)
        self.SideLine.setHidden(False)
        try:
            side = float(self.SideLine.text())

        except ValueError:
            self.AnswerLine.setText("invalid")
            return
        self.square_A = side * side
        self.square_P = 4 * side
        self.AnswerLine.setText(f"Area = {self.square_A} \n Perimeter = {self.square_P}")


    def Rectangle(self):
        '''
        calculate the area and perimeter of rectangle
        '''
        pass


    def Parallelogram(self):
        '''
        calculate the area and perimeter of parallelogram
        '''
        pass



    def Triangle(self):
        '''
               calculate the area and perimeter of triangle
        '''
        pass

    def Rhombus(self):
        '''
               calculate the area and perimeter of rhombus
               '''
        pass

    def Submit(self):
        '''

        :return:
        '''
        self.AnswerLine.setHidden(False)

        if self.CircleButton.isChecked():
            self.Circle()
        elif self.SquareButton.isChecked():
            self.Square()
        else:
            self.AnswerLine.setText("Choose shape first")


        #call the function

    def Clear(self):
        # clear all the radio button
        self.group_button.setExclusive(False)
        self.CircleButton.setChecked(False)
        self.SquareButton.setChecked(False)
        self.TriangleButton.setChecked(False)
        self.RectangleButton.setChecked(False)
        self.ParalButton.setChecked(False)
        self.RhombusButton.setChecked(False)
        #hide all the label and line input box
        self.RadiusLabel.setHidden(True)
        self.RadiusLine.setHidden(True)
        self.LengthLabel.setHidden(True)
        self.LengthLine.setHidden(True)
        self.BaseLabel.setHidden(True)
        self.BaseLine.setHidden(True)
        self.SideLabel.setHidden(True)
        self.SideLine.setHidden(True)
        self.WidthLabel.setHidden(True)
        self.WidthLine.setHidden(True)
        self.HeightLabel.setHidden(True)
        self.HeightLine.setHidden(True)
        self.AnswerLine.setHidden(True)






