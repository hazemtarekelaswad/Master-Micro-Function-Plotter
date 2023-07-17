from PySide2.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton, 
    QMessageBox, 
    QDesktopWidget, 
    QGridLayout, 
    QGroupBox, 
    QTextEdit, 
    QHBoxLayout, 
    QVBoxLayout, 
    QLabel
)
from PySide2.QtGui import QIcon, QCursor
import sys
import numpy as np



from InputParser import InputParser
from Plotter import Plotter

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setFixedSize(1300, 800)
        self.setWindowIcon(QIcon("sinus.png"))
        self.centerWindow()
        self.mainGrid = self.createMainGrid()
        self.setLayout(self.mainGrid)

    def centerWindow(self):
        rect = self.frameGeometry()
        rect.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(rect.topLeft())


    def createPushButton(self, text):
        pushButton = QPushButton(text, self)
        return pushButton
        
    
    def createSubGrid(self):
        self.fx = QTextEdit()
        self.xmin = QTextEdit()
        self.xmax = QTextEdit()
        plotButton = QPushButton("Plot", self)

        grid = QGridLayout()
        grid.addWidget(QLabel("f(x): "), 0, 0)
        grid.addWidget(self.fx, 0, 1)
        grid.addWidget(QLabel("X min: "), 1, 0)
        grid.addWidget(self.xmin, 1, 1)
        grid.addWidget(QLabel("X max: "), 2, 0)
        grid.addWidget(self.xmax, 2, 1)
        grid.addWidget(plotButton, 3, 0, 1, 2)

        plotButton.clicked.connect(self.plotButtonAction)

        return grid


    def createMainGrid(self):
        grid = QGridLayout()
        grid.addLayout(self.createSubGrid(), 0, 0)

        # Todo: Matplotlib plot image
        plotImage = Plotter(self, np.zeros((5, 5)), np.zeros((5, 5)))
        grid.addWidget(plotImage, 0, 1)
        return grid
    
    def createErrorMessageBox(self, text):
        errorBox = QMessageBox()
        errorBox.setWindowTitle("Error")
        errorBox.setText(text)
        errorBox.exec_()
    
    def plotButtonAction(self):
        try:
            Xs, Ys = InputParser(self.fx.toPlainText(), self.xmin.toPlainText(), self.xmax.toPlainText(), 0.1).parse()
            self.mainGrid.addWidget(Plotter(self, Xs, Ys), 0, 1)
        except Exception as e:
            self.createErrorMessageBox(str(e))
  
            

