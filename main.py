import ctypes
import _thread
import time
# import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QGridLayout
from MainWndUi import Ui_MainWindow
from lineplt import CLineFigure
from threedplt import C3DFigure
from mdata import CDataReq


exit_timer = False

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ui_initial()
        self.termination = False

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,
                                               '光纤温度场',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.stop()
        else:
            event.ignore()


    def ui_initial(self):
        self.data_req = CDataReq()
        self.obj_line = CLineFigure(width=3, height=2, dpi=100)
        self.obj_3d = C3DFigure(width=3, height=2, dpi=100)
        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.setSpacing(1)
        self.gridlayout.setContentsMargins(1,1,1,1)
        self.gridlayout.addWidget(self.obj_line, 0, 0)
        self.gridlayout.addWidget(self.obj_3d, 1, 0)
        self.gridlayout.setRowStretch(0, 1)
        self.gridlayout.setRowStretch(1, 2)
        # self.timer = threading.Timer(1, self.func)

    def func(self):
        count = 0
        while self.termination == False:
            time.sleep(0.5)
            self.obj_line.plot_line()
            count += 1
            print("%s" % (time.ctime(time.time())))
        # if exit_timer:
        #     return
        # time.sleep(1)
        # data = self.data_req.get_data()
        # print(data)
        # self.timer = threading.Timer(1, self.func)
        # self.timer.start()


    def start(self):
        _thread.start_new_thread(self.func,())

    def stop(self):
        self.termination = True
        # self.timer.start()

    # def plotcos(self):
    #     t = np.arange(0.0, 5.0, 0.01)
    #     s = np.cos(2 * np.pi * t)
    #     self.F.axes.plot(t, s)
    #     self.F.fig.suptitle("cos")

    # def plotother(self):
    #     F1 = CFigure(width=5, height=4, dpi=100)
    #     F1.fig.suptitle("Figuer_4")
    #     F1.axes1 = F1.fig.add_subplot(221)
    #     x = np.arange(0, 50)
    #     y = np.random.rand(50)
    #     F1.axes1.hist(y, bins=50)
    #     F1.axes1.plot(x, y)
    #     F1.axes1.bar(x, y)
    #     F1.axes1.set_title("hist")
    #     F1.axes2 = F1.fig.add_subplot(222)
    #
    #     ## 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
    #     x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
    #     F1.axes2.plot(x, y)
    #     F1.axes2.set_title("line")
    #     # 散点图
    #     F1.axes3 = F1.fig.add_subplot(223)
    #     F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
    #     F1.axes3.set_title("scatter")
    #     # 折线图
    #     F1.axes4 = F1.fig.add_subplot(224)
    #     x = np.arange(0, 5, 0.1)
    #     F1.axes4.plot(x, np.sin(x), x, np.cos(x))
    #     F1.axes4.set_title("sincos")
    #     self.gridlayout.addWidget(F1, 0, 2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("TempID")
    main_window = MainWindow()
    main_window.start()
    # main_window.resize(250, 150)
    main_window.show()
    sys.exit(app.exec_())



