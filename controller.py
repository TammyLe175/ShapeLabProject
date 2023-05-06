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
        self.TriangleButton.toggled.connect(self.Triangle)
        self.RectangleButton.toggled.connect(self.Rectangle)
        self.ParalButton.toggled.connect(self.Parallelogram)
        self.RhombusButton.toggled.connect(self.Rhombus)

        #answer and clear button
        self.AnswerButton.clicked.connect(lambda: self.Submit())
        self.ClearButton.clicked.connect(lambda: self.Clear())

        # set all input box and label in hidden
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
        self.rectangle_A = 0.00
        self.rectangle_P = 0.00
        self.triangle_A = 0.00
        self.triangle_P = 0.00
        self.parall_A = 0.00
        self.parall_P = 0.00
        self.rhombus_A = 0.00
        self.rhombus_P = 0.00
    def Circle(self):
        """
        show radius label and line
        calculate the area and perimeter of circle
        :return: the area and perimeter in Answer box if user enter string return invalid
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
        show side label and line
        calculate the area and perimeter of square
        :return: area and perimeter or invalid in Answer box
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
        show length, width label and line
        calculate the area and perimeter of rectangle
        :return: area and perimeter or invalid in Answer box
        '''
        self.LengthLabel.setHidden(False)
        self.LengthLine.setHidden(False)
        self.WidthLabel.setHidden(False)
        self.WidthLine.setHidden(False)
        try:
            length = float(self.LengthLine.text())
            width = float(self.WidthLine.text())

        except ValueError:
            self.AnswerLine.setText("invalid")
            return
        self.rectangle_A = length * width
        self.rectangle_P = (2 * length) + (2 * width)
        self.AnswerLine.setText(f"Area = {self.rectangle_A} \n Perimeter = {self.rectangle_P}")


    def Parallelogram(self):
        '''
        show base, height label and line
        calculate the area and perimeter of parallelogram
        :return: area and perimeter or invalid in Answer box
        '''
        self.BaseLabel.setHidden(False)
        self.BaseLine.setHidden(False)
        self.HeightLabel.setHidden(False)
        self.HeightLine.setHidden(False)
        try:
            base = float(self.BaseLine.text())
            height = float(self.HeightLine.text())

        except ValueError:
            self.AnswerLine.setText("invalid")
            return
        self.parall_A = base * height
        self.parall_P = 2 * (base + height)
        self.AnswerLine.setText(f"Area = {self.parall_A} \n Perimeter = {self.parall_P}")

    def Triangle(self):
        '''
        show side,base,height label and line
        calculate the area and perimeter of triangle
        :return: area and perimeter or invalid in Answer box
        '''
        self.SideLabel.setHidden(False)
        self.SideLine.setHidden(False)
        self.BaseLabel.setHidden(False)
        self.BaseLine.setHidden(False)
        self.HeightLabel.setHidden(False)
        self.HeightLine.setHidden(False)
        try:
            side = float(self.SideLine.text())
            base = float(self.BaseLine.text())
            height = float(self.HeightLine.text())

        except ValueError:
            self.AnswerLine.setText("invalid")
            return
        self.triangle_A = 0.5 * base * height
        self.triangle_P = (2 * side) + base
        self.AnswerLine.setText(f"Area = {self.triangle_A} \n Perimeter = {self.triangle_P}")
    def Rhombus(self):
        '''
        show base,height label and line
        calculate the area and perimeter of Rhombus
        :return: area and perimeter or invalid in Answer box
               '''
        self.BaseLabel.setHidden(False)
        self.BaseLine.setHidden(False)
        self.HeightLabel.setHidden(False)
        self.HeightLine.setHidden(False)
        try:
            base = float(self.BaseLine.text())
            height = float(self.HeightLine.text())

        except ValueError:
            self.AnswerLine.setText("invalid")
            return
        self.rhombus_A = base * height
        self.rhombus_P = 4 * base
        self.AnswerLine.setText(f"Area = {self.rhombus_A} \n Perimeter = {self.rhombus_P}")

    def Submit(self):
        '''
        show Answer box
        check if a radio button is checked do call the function
        '''
        self.AnswerLine.setHidden(False)

        if self.CircleButton.isChecked():
            self.Circle()
        elif self.SquareButton.isChecked():
            self.Square()
        elif self.TriangleButton.isChecked():
            self.Triangle()
        elif self.RectangleButton.isChecked():
            self.Rectangle()
        elif self.ParalButton.isChecked():
            self.Parallelogram()
        elif self.RhombusButton.isChecked():
            self.Rhombus()
        else:
            self.AnswerLine.setText("Choose shape first")

    def Clear(self):
        # clear all the radio button
        self.group_button.setExclusive(False)
        self.CircleButton.setChecked(False)
        self.SquareButton.setChecked(False)
        self.TriangleButton.setChecked(False)
        self.RectangleButton.setChecked(False)
        self.ParalButton.setChecked(False)
        self.RhombusButton.setChecked(False)
        #hide and clear all the label and line input box
        self.RadiusLabel.setHidden(True)
        self.RadiusLine.setHidden(True)
        self.RadiusLine.clear()
        self.LengthLabel.setHidden(True)
        self.LengthLine.setHidden(True)
        self.LengthLine.clear()
        self.BaseLabel.setHidden(True)
        self.BaseLine.setHidden(True)
        self.BaseLine.clear()
        self.SideLabel.setHidden(True)
        self.SideLine.setHidden(True)
        self.SideLine.clear()
        self.WidthLabel.setHidden(True)
        self.WidthLine.setHidden(True)
        self.WidthLine.clear()
        self.HeightLabel.setHidden(True)
        self.HeightLine.setHidden(True)
        self.HeightLine.clear()
        self.AnswerLine.setHidden(True)
        self.AnswerLine.clear()






