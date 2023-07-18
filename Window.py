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
    QLabel,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QStyle
)
from PySide2.QtGui import QIcon, QCursor, QFont, QGuiApplication
from PySide2 import QtCore
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
        window = self.window()
        window.setGeometry(
            QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                window.size(),
                QGuiApplication.primaryScreen().availableGeometry(),
            ),
        )

    def createPushButton(self, text):
        pushButton = QPushButton(text, self)
        return pushButton

    def createMainGrid(self):

        self.fx = QLineEdit()
        self.xmin = QDoubleSpinBox()
        self.xmax = QDoubleSpinBox()

        self.fxLabel = QLabel("f(x): ")
        self.fxLabel.setFont(QFont("Cambria", 15, 5, True))
        self.xminLabel = QLabel("X min: ")
        self.xminLabel.setFont(QFont("Cambria", 15, 5, True))
        self.xmaxLabel = QLabel("X max: ")
        self.xmaxLabel.setFont(QFont("Cambria", 15, 5, True))

        self.fx.setPlaceholderText("i.e. 9*x^2+6")

        self.xmin.setRange(-1000000000, 1000000000)
        self.xmax.setRange(-1000000000, 1000000000)

        self.xmin.setValue(0)
        self.xmax.setValue(1)

        self.xmin.setDecimals(3)
        self.xmax.setDecimals(3)

        self.fx.setFixedHeight(50)
        self.xmin.setFixedHeight(50)
        self.xmax.setFixedHeight(50)

        self.fx.setFont(QFont("Cambria", 15, 10, True))
        self.xmin.setFont(QFont("Cambria", 15, 10, True))
        self.xmax.setFont(QFont("Cambria", 15, 10, True))

        self.plotButton = QPushButton("Plot", self)
        self.plotButton.setFont(QFont("Cambria", 15, 10, True))
        self.plotButton.setFixedHeight(75)
        self.plotButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        grid = QGridLayout()
        grid.setHorizontalSpacing(20)
        grid.addWidget(self.fxLabel, 0, 0)
        grid.addWidget(self.fx, 0, 1)
        grid.addWidget(self.xminLabel, 1, 0)
        grid.addWidget(self.xmin, 1, 1)
        grid.addWidget(self.xmaxLabel, 2, 0)
        grid.addWidget(self.xmax, 2, 1)
        grid.addWidget(self.plotButton, 3, 0, 1, 2)

        plotImage = Plotter(self, np.zeros((5, 5)), np.zeros((5, 5)))
        grid.addWidget(plotImage, 0, 2, 4, 1)

        grid.setColumnMinimumWidth(0, 100)
        grid.setColumnMinimumWidth(1, 300)
        grid.setColumnMinimumWidth(2, 800)

        self.plotButton.clicked.connect(self.plotButtonAction)
        return grid

    def createErrorMessageBox(self, text):
        self.errorMsg = text
        errorBox = QMessageBox().critical(self, "Error | Invalid Input", text)

    def plotButtonAction(self):
        try:
            Xs, Ys = InputParser(
                self.fx.text(), self.xmin.text(), self.xmax.text()).parse()
            self.mainGrid.itemAtPosition(0, 2).widget().__del__()
            self.mainGrid.addWidget(Plotter(self, Xs, Ys), 0, 2, 4, 1)
        except Exception as e:
            self.createErrorMessageBox(str(e))
