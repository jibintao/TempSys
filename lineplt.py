import numpy as np
import random
import matplotlib

# import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.rcParams["axes.unicode_minus"] = False
zhfont1 = fm.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
matplotlib.use("Qt5Agg")

class CLineFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        # plt.use('seaborn')
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(CLineFigure,self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        # plt.ion()
        # plt.grid(True)
        # self.axes.plot(0, 0, 'C1', label='左')
        # self.axes.plot(0, 0, 'C2', label='中')
        # self.axes.plot(0, 0, 'C3', label='右')
        # self.axes.legend()

        # t = np.arange(0.0, 3.0, 0.01)
        # s = np.sin(2 * np.pi * t)
        # self.axes.plot(t, s, color='red', linewidth=5, linestyle='--')

        # self.fig.suptitle('温度变化曲线', fontproperties=zhfont1)

    def plot_line(self):
        # self.axes0 = self.fig.add_subplot(111)
        self.axes.cla()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        th = np.linspace(0, random.randint(0,9) * np.pi, 128)
        # self.axes.plot(t, s, color='red', linewidth=2, linestyle='--')
        # self.axes.plot(th, np.cos(th), 'C1', label='左', fontproperties=zhfont1)
        # self.axes.plot(th, np.sin(th), 'C2', label='中', fontproperties=zhfont1)
        # self.axes.plot(th, np.tan(th), 'C3', label='右', fontproperties=zhfont1)
        self.axes.plot(th, np.cos(th), 'C1', label='左')
        self.axes.plot(th, np.sin(th), 'C2', label='中')
        self.axes.plot(th, 2*np.cos(th), 'C3', label='右')
        self.axes.legend()

        # self.axes.legend()
        self.fig.canvas.draw_idle()