import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Plotter(FigureCanvas):
    def __init__(self, parent, Xs, Ys):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        super().__init__(self.fig)
        self.Xs = Xs
        self.Ys = Ys
        self.setParent(parent)
        self.ax.plot(self.Xs, self.Ys)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.set_title("Plot of the function f(x)")
        self.ax.grid()
    
    def __del__(self):
        plt.close(self.fig)