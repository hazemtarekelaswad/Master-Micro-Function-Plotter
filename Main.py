
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PySide2.QtGui import QIcon, QCursor
import sys

from Window import Window
import numpy as np

def main():
    app = QApplication()

    window = Window()
    window.show()

    app.exec_()

def test():
    print(np.linspace(2, 54.5).shape)


if __name__ == '__main__':
    main()