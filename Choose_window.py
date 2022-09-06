from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
from Series_window import Eminem
from Statistic_window import SnoopDog
from Subset_window import DoctorDre
from Textual_window import RandyOrton

class IceCube(QMainWindow):
    def __init__(self):
        super(IceCube, self).__init__()

        uic.loadUi("choose.ui", self)

        # define content:
        self.hello_label = self.findChild(QLabel, "hello_label")
        self.series_button = self.findChild(QPushButton, "series_button")
        self.statistic_button = self.findChild(QPushButton, "statistic_button")
        self.subset_button = self.findChild(QPushButton, "subset_button")
        self.text_button = self.findChild(QPushButton, "text_button")
        self.exit_button = self.findChild(QPushButton, "exit_button")

        # call defined functions from here:
        self.series_button.clicked.connect(self.GoToSeries)
        self.statistic_button.clicked.connect(self.GoToStatistics)
        self.subset_button.clicked.connect(self.GoToSubset)
        self.text_button.clicked.connect(self.GoToTextual)
        self.exit_button.clicked.connect(lambda: self.close())


        self.show()
# ------------------------------------------ start -------------------------------------- #
    # define method for next windows:
    def GoToSeries(self):
        self.window_series = QMainWindow()
        self.water = Eminem()
        self.close()
    
    def GoToStatistics(self):
        self.window_statistics = QMainWindow()
        self.dog = SnoopDog()
        self.close()
    
    def GoToSubset(self):
        self.window_subset = QMainWindow()
        self.doctor = DoctorDre()
        self.close()
    
    def GoToTextual(self):
        self.window_text = QMainWindow()
        self.randy = RandyOrton()
        self.close()

# ------------------------------------------- end --------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ice = IceCube()
    sys.exit(app.exec_())