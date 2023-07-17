import cexprtk as ctk
import numpy as np

class InputParser:
    def __init__(self, fx: str, xmin: str, xmax: str, step: float):
        self.fx = fx
        self.xmin = xmin
        self.xmax = xmax
        self.step = step
    
    def __parseFx(self):
        Xs = np.linspace(self.xmin, self.xmax)
        Ys = np.zeros(Xs.shape)
        try:
            for i in range(Ys.shape[0]):
                Ys[i] = ctk.evaluate_expression(self.fx, { "x": Xs[i] })
        except:
            raise Exception("Error while parsing f(x)")
        return Xs, Ys

    def __isXMinValid(self):
        if self.xmin == "":
            return False, "Xmin shouldn't be empty"
        return True, ""

    def __isXMaxValid(self):
        if self.xmax == "":
            return False, "Xmax shouldn't be empty"
        return True, ""
    
    def __isFxValid(self):
        return True, ""

    def __parseXMin(self):
        try:
            self.xmin = float(self.xmin)
        except:
            raise Exception("Xmin should be numeric")
    def __parseXMax(self):
        try:
            self.xmax = float(self.xmax)
        except:
            raise Exception("Xmax should be numeric")
        
    
    def parse(self):
        isXMinValid, xMinErrorMsg = self.__isXMinValid()
        isXMaxValid, xMaxErrorMsg = self.__isXMaxValid()
        isFxValid, fxErrorMsg = self.__isFxValid()

        if not isXMinValid:
            raise Exception(xMinErrorMsg)
        if not isXMaxValid:
            raise Exception(xMaxErrorMsg)
        if not isFxValid:
            raise Exception(fxErrorMsg)
        self.__parseXMin()
        self.__parseXMax()

        if self.xmin >= self.xmax:
            raise Exception("Xmin should be less than Xmax")

        Xs, Ys = self.__parseFx()
        return Xs, Ys



