from PyQt5.QtWidgets import QLabel, QSizePolicy, QVBoxLayout,QHBoxLayout,QGridLayout, QWidget, QScrollArea, QGroupBox, QMainWindow, QScrollBar, QApplication
import Sim

import sys

class Simulator:
    @classmethod
    def run(cls):
        app = QApplication(sys.argv)

        m = QMainWindow()
        m.resize(1000, 1000)
        w = Sim.Mod(m)

        m.setCentralWidget(w)
        m.show()

        sys.exit(app.exec_())

