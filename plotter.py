import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QTimer
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np


class PlotterWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PlotterWidget, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        C = pg.glColor('w')

        self.view = gl.GLViewWidget()
        layout.addWidget(self.view)

        p = self.calc(2)
        self.scatItem = gl.GLScatterPlotItem(pos=p, color=C, size=2)
        self.view.addItem(self.scatItem)

        g = gl.GLGridItem()
        g.setSize(200, 200)
        g.setSpacing(5, 5)
        self.view.addItem(g)

    def plot(self, number):
        p = self.calc(number)
        self.scatItem.setData(pos=p)

    def calc(self, number):
        X = np.linspace(0, 20, 100)
        Y = np.cos(X * np.pi / 4 + number)
        Z = np.sin(X * np.pi / 4 + number)
        p = np.array([X, Y, Z])
        return p.transpose()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.plotter = PlotterWidget()
        self.setCentralWidget(self.plotter)
        w = 1920
        h = 1080
        self.resize(w, h)
        self.plotpos = 0

        self._update()

    def _update(self):
        random_number = np.random.rand(1) ** 100
        random_matrix = np.random.rand(3, 3)

        self.plotpos += 0.1
        self.plotter.plot(self.plotpos)
        QTimer.singleShot(200, self._update)


def _main():
    useGUI = '-no-gui' not in sys.argv
    app = QtWidgets.QApplication(sys.argv) if useGUI else QtWidgets.QCoreApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(_main())
