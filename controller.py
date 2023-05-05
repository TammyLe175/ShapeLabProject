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

        #create variable
        self.circle_area = 0.00
        self.circle_perimeter = 0.00
        #self.square_area = 0.00
        #self.square_perimeter = 0.00



    def Circle(self):
        """
        calculate the area and perimeter of circle
        """
        try:
            self.RadiusLabel.setHidden(False)
            self.RadiusLine.setHidden(False)
            radius = float(self.RadiusLine.text())
            self.circle_area = pi * (radius ** 2)
            self.circle_perimeter = 2 * pi * radius

        except ValueError:
            self.AnswerLine.setText("Invalid")


    def Square(self):
        '''
        calculate the area and perimeter of square
        :return: area and perimeter
        '''

       # self.SideLabel.setHidden(False)
       # self.SideLine.setHidden(False)
       # side = float(self.SideLine.text())
       # self.square_area = side * side
       # self.square_perimeter = 4 * side



    def Rectangle(self):
        '''
        calculate the area and perimeter of rectangle
        :return: area and perimeter
        '''
        pass


    def Parallelogram(self):
        '''
        calculate the area and perimeter of parallelogram
        :return: area and perimeter
        '''
        pass



    def Triangle(self):
        '''
               calculate the area and perimeter of triangle
               :return: area and perimeter
        '''
        pass

    def Rhombus(self):
        '''
               calculate the area and perimeter of rhombus
               :return: area and perimeter
               '''
        pass

    def Submit(self):
        '''

        :return:
        '''
        self.AnswerLine.setHidden(False)

        if self.CircleButton.toggled.connect(self.Circle):
            self.AnswerLine.setText(f'Area of circle = {self.circle_area}\nPerimeter of circle = {self.circle_perimeter}\n')
        elif self.SquareButton.toggled.connect(self.Square):
                self.AnswerLine.setText(f'Area of square = {self.square_area}\nPerimeter of square = {self.square_perimeter}\n')
