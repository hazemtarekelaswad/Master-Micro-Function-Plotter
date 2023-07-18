from PySide2.QtGui import QFont

class Constants:
    WINDOW_SIZE = (1300, 800)
    WINDOW_TITLE = "Function Plotter"
    WINDOW_ICON = "sinus.png"

    FONT_FAMILY = "Cambria"
    FONT_SIZE = 15
    FONT_WEIGHT = 10
    FONT_ITALIC = True

    LABEL_FONT = (FONT_FAMILY, FONT_SIZE, FONT_WEIGHT // 2, FONT_ITALIC)
    INPUT_FONT = (FONT_FAMILY, FONT_SIZE, FONT_WEIGHT, FONT_ITALIC)
    TITLE_FONT = (FONT_FAMILY, FONT_SIZE * 2, QFont.Bold, False)

    PLOT_BUTTON_TEXT = "Plot"
    PLOT_BUTTON_HEIGHT = 75

    FX_PLACEHOLDER_TEXT = "i.e. 9*x^2+6"
    INPUT_HEIGHT = 50

    X_MIN_RANGE = (-1000000000, 1000000000)
    X_MAX_RANGE = (-1000000000, 1000000000)

class ErrorMessages:
    INVALID_FX = "Error while parsing f(x)"
    INVALID_EMPTY_FX = "f(x) shouldn't be empty"
    INVALID_X_MIN = "Xmin shouldn't be empty"
    INVALID_X_MAX = "Xmax shouldn't be empty"
    INVALID_X_MIN_MAX = "Xmin should be less than Xmax"
    INVALID_X_MIN_TYPE = "Xmin should be numeric"
    INVALID_X_MAX_TYPE = "Xmax should be numeric"

