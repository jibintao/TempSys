import numpy as np
import matplotlib
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# matplotlib.use("Qt5Agg")


class C3DFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(C3DFigure,self).__init__(self.fig)
        zhfont1 = fm.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
        self.axes = self.fig.add_subplot(111)
        # self.fig.suptitle(u'温度分布图', fontproperties=zhfont1)

    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes0.plot(t, s)

    def plotcos(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s, color='red', linewidth=5, linestyle='--')