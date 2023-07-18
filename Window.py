'''
This file contains the Window class which is used to create 
the main window of the program and all of the GUI functionalities.
'''

# Pyside2 imports
from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
    QMessageBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QDoubleSpinBox,
    QStyle
)
from PySide2.QtGui import QIcon, QCursor, QFont, QGuiApplication
from PySide2 import QtCore

# Other imports
import numpy as np

# Local imports
from InputParser import InputParser
from Plotter import Plotter
from Constants import Constants


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(Constants.WINDOW_TITLE)
        self.setFixedSize(*Constants.WINDOW_SIZE)
        self.setWindowIcon(QIcon(Constants.WINDOW_ICON))
        self.centerWindow()
        self.mainGrid = self.createMainGrid()
        self.setLayout(self.mainGrid)

    # This function is used to center the window on the screen
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

    # This function is used to create a push button
    def createPushButton(self, text):
        pushButton = QPushButton(text, self)
        return pushButton

    # This function is used to create an error message box
    def createErrorMessageBox(self, text):
        self.errorMsg = text
        _ = QMessageBox().critical(self, "Error | Invalid Input(s)", text)

    # This function is used to create the main grid of the window
    def createMainGrid(self):
        # Initialize and configure the main input widgets
        self.fx = QLineEdit()
        self.xmin = QDoubleSpinBox()
        self.xmax = QDoubleSpinBox()

        self.fxLabel = QLabel("f(x): ")
        self.fxLabel.setFont(QFont(*Constants.LABEL_FONT))
        self.xminLabel = QLabel("X min: ")
        self.xminLabel.setFont(QFont(*Constants.LABEL_FONT))
        self.xmaxLabel = QLabel("X max: ")
        self.xmaxLabel.setFont(QFont(*Constants.LABEL_FONT))

        self.fx.setPlaceholderText(Constants.FX_PLACEHOLDER_TEXT)

        self.xmin.setRange(*Constants.X_MIN_RANGE)
        self.xmax.setRange(*Constants.X_MAX_RANGE)

        self.xmin.setValue(0)
        self.xmax.setValue(1)

        self.xmin.setDecimals(3)
        self.xmax.setDecimals(3)

        self.fx.setFixedHeight(Constants.INPUT_HEIGHT)
        self.xmin.setFixedHeight(Constants.INPUT_HEIGHT)
        self.xmax.setFixedHeight(Constants.INPUT_HEIGHT)

        self.fx.setFont(QFont(*Constants.INPUT_FONT))
        self.xmin.setFont(QFont(*Constants.INPUT_FONT))
        self.xmax.setFont(QFont(*Constants.INPUT_FONT))

        self.plotButton = QPushButton("Plot", self)
        self.plotButton.setFont(QFont(*Constants.INPUT_FONT))
        self.plotButton.setFixedHeight(Constants.PLOT_BUTTON_HEIGHT)
        self.plotButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        # Create the main grid and add the widgets to it
        grid = QGridLayout()
        grid.addWidget(self.fxLabel, 0, 0)
        grid.addWidget(self.fx, 0, 1)
        grid.addWidget(self.xminLabel, 1, 0)
        grid.addWidget(self.xmin, 1, 1)
        grid.addWidget(self.xmaxLabel, 2, 0)
        grid.addWidget(self.xmax, 2, 1)
        grid.addWidget(self.plotButton, 3, 0, 1, 2)

        plotImage = Plotter(self, np.zeros((5, 5)), np.zeros((5, 5)))
        grid.addWidget(plotImage, 0, 2, 4, 1)

        # Configure the grid
        grid.setHorizontalSpacing(20)
        grid.setColumnMinimumWidth(0, 100)
        grid.setColumnMinimumWidth(1, 300)
        grid.setColumnMinimumWidth(2, 800)

        # Connect the plot button to its action
        self.plotButton.clicked.connect(self.plotButtonAction)
        return grid

    
    # This function is used to handle the plot button functionality
    def plotButtonAction(self):
        try:
            # Parse the input, then plot the points returned by the parser
            Xs, Ys = InputParser(
                self.fx.text(), self.xmin.text(), self.xmax.text()).parse()
            self.mainGrid.itemAtPosition(0, 2).widget().close()
            self.mainGrid.addWidget(Plotter(self, Xs, Ys), 0, 2, 4, 1)
        except Exception as e:
            # If an error occurs, show an error message box
            self.createErrorMessageBox(str(e))
