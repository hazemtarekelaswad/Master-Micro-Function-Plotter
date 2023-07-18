'''
The main file of the program. This file is used to run the program.
'''

from PySide2.QtWidgets import QApplication
from Window import Window

def main():
    # Create the Qt Application
    app = QApplication()

    # Create and show a window
    window = Window()
    window.show()

    # Run the main Qt loop
    app.exec_()


if __name__ == '__main__':
    main()