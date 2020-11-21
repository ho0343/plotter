import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QTimer
import pyqtgraph as pg


class PlotterWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PlotterWidget, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        pw = pg.PlotWidget()
        pw.plot([1, 2, 3, 4])
        layout.addWidget(pw)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.plotter = PlotterWidget()
        self.setCentralWidget(self.plotter)

        self._update()

    def _update(self):
        QTimer.singleShot(1000, self._update)


def _main():
    useGUI = '-no-gui' not in sys.argv
    app = QtWidgets.QApplication(sys.argv) if useGUI else QtWidgets.QCoreApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(_main())
