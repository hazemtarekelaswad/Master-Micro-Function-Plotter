'''
This file contains the InputParser class which is used to validate and parse all input data.
'''

import cexprtk as ctk
import numpy as np
from Constants import ErrorMessages

class InputParser:
    def __init__(self, fx: str, xmin: str, xmax: str):
        self.fx = fx
        self.xmin = xmin
        self.xmax = xmax
    

    ################### Utility Functions: #######################

    # This function is used to parse the function f(x) and returns the Xs and Ys points
    # based on the minimum and maximum x values
    def __parseFx(self):
        Xs = np.linspace(self.xmin, self.xmax)
        Ys = np.zeros(Xs.shape)
        try:
            for i in range(Ys.shape[0]):
                Ys[i] = ctk.evaluate_expression(self.fx, { "x": Xs[i] })
        except:
            raise Exception(ErrorMessages.INVALID_FX)
        return Xs, Ys

    # These functions are used to validate the input data
    def __isXMinValid(self):
        if self.xmin == "":
            return False, ErrorMessages.X_MIN_EMPTY
        return True, ""

    def __isXMaxValid(self):
        if self.xmax == "":
            return False, ErrorMessages.X_MAX_EMPTY
        return True, ""
    
    def __isFxValid(self):
        if self.fx == "":
            return False, ErrorMessages.INVALID_EMPTY_FX
        return True, ""

    # These functions are used to parse the input data if they are not floats
    def __parseXMin(self):
        try:
            self.xmin = float(self.xmin)
        except:
            raise Exception(ErrorMessages.INVALID_X_MIN_TYPE)
    def __parseXMax(self):
        try:
            self.xmax = float(self.xmax)
        except:
            raise Exception(ErrorMessages.INVALID_X_MAX_TYPE)
        
    
    ################### Public Functions: #######################
    # This is the exposed function that is used to parse the input data
    def parse(self):
        isXMinValid, xMinErrorMsg = self.__isXMinValid()
        isXMaxValid, xMaxErrorMsg = self.__isXMaxValid()
        isFxValid, fxErrorMsg = self.__isFxValid()

        if not isFxValid:
            raise Exception(fxErrorMsg)
        if not isXMinValid:
            raise Exception(xMinErrorMsg)
        if not isXMaxValid:
            raise Exception(xMaxErrorMsg)
        self.__parseXMin()
        self.__parseXMax()

        if self.xmin >= self.xmax:
            raise Exception(ErrorMessages.INVALID_X_MIN_MAX)

        Xs, Ys = self.__parseFx()
        return Xs, Ys



