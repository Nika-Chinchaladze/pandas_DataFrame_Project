from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QTableWidget, QLineEdit, QComboBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QIntValidator
from PyQt5 import uic
import pandas as pd
import numpy as np

class Eminem(QMainWindow):
    def __init__(self):
        super(Eminem, self).__init__()

        uic.loadUi("series.ui", self)

        # define content:
        self.hello_label = self.findChild(QLabel, "hello_label")
        self.title_label = self.findChild(QLabel, "title_label")
        self.create_label = self.findChild(QLabel, "create_label")
        self.choose_label = self.findChild(QLabel, "choose_label")
        self.numpy_label = self.findChild(QLabel, "numpy_label")
        self.dict_label = self.findChild(QLabel, "dict_label")
        self.key_label = self.findChild(QLabel, "key_label")
        self.value_label = self.findChild(QLabel, "value_label")
        self.answer_label = self.findChild(QLabel, "answer_label")
        self.head_label = self.findChild(QLabel, "head_label")
        self.list_label = self.findChild(QLabel, "list_label")
        self.scalar_label = self.findChild(QLabel, "scalar_label")
        self.file_label = self.findChild(QLabel, "file_label")
        self.result_label = self.findChild(QLabel, "result_label")

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")
        self.create_button = self.findChild(QPushButton, "create_button")
        self.show_button = self.findChild(QPushButton, "show_button")

        self.range_line = self.findChild(QLineEdit, "range_line")
        self.size_line = self.findChild(QLineEdit, "size_line")
        self.key_line = self.findChild(QLineEdit, "key_line")
        self.value_line = self.findChild(QLineEdit, "value_line")
        self.head_line = self.findChild(QLineEdit, "head_line")
        self.list_line = self.findChild(QLineEdit, "list_line")
        self.scalar_line_1 = self.findChild(QLineEdit, "scalar_line_1")
        self.scalar_line_2 = self.findChild(QLineEdit, "scalar_line_2")
        self.filename_line = self.findChild(QLineEdit, "filename_line")
        self.column_line = self.findChild(QLineEdit, "column_line")

        self.table_widget = self.findChild(QTableWidget, "table_widget")
        self.line_1 = self.findChild(QFrame, "line_1")
        self.choose_box = self.findChild(QComboBox, "choose_box")
        
        #set int validator:
        Only_Int = QIntValidator()
        self.range_line.setValidator(Only_Int)
        self.size_line.setValidator(Only_Int)
        self.list_line.setValidator(Only_Int)
        self.scalar_line_1.setValidator(Only_Int)
        self.scalar_line_2.setValidator(Only_Int)

        # set placeholder - hint texts:
        self.range_line.setPlaceholderText("highest number")
        self.size_line.setPlaceholderText("size")
        self.list_line.setPlaceholderText("highest number")
        self.scalar_line_1.setPlaceholderText("number")
        self.scalar_line_2.setPlaceholderText("quantity")
        self.filename_line.setPlaceholderText("filename.csv")
        self.column_line.setPlaceholderText("column name")

        # set some button disabled:
        self.display_button.setEnabled(False)

        # call defined method from here:
        self.create_button.clicked.connect(self.Create_Series)
        self.display_button.clicked.connect(self.Display_Series)
        self.show_button.clicked.connect(self.Show_columns)
        self.back_button.clicked.connect(self.GoBack)

        self.show()

# ----------------------------------------- start --------------------------------------- #
    # define method for back button:
    def GoBack(self):
        from Choose_window import IceCube
        self.window_first = QMainWindow()
        self.ice = IceCube()
        self.close()

    # define background colors:
    def Green(self):
        self.answer_label.setStyleSheet("background-color: rgb(155, 255, 184);")

    def White(self):
        self.answer_label.setStyleSheet("background-color: rgb(240, 240, 240);")
    
    def White_2(self):
        self.result_label.setStyleSheet("background-color: rgb(240, 240, 240);")
    
    def Red_1(self):
        self.answer_label.setStyleSheet("background-color: rgb(255, 178, 216);")
    
    def Red_2(self):
        self.result_label.setStyleSheet("background-color: rgb(255, 178, 216);")
    
    # define method for show button:
    def Show_columns(self):
        filename = self.filename_line.text()
        if len(filename) > 0:
            try:
                entered_file = pd.read_csv(f"{filename}")
                column_list = list(entered_file.columns)
                self.result_label.setText(f"{column_list}")
                self.White_2()
            except FileNotFoundError:
                self.result_label.setText("File does not exists!")
                self.Red_2()
        else:
            self.result_label.setText("Please Enter File Name!")
            self.Red_2()

    # define clean method:
    def Clean_lines(self):
        self.head_line.setText("")
        self.range_line.setText("")
        self.size_line.setText("")
        self.list_line.setText("")
        self.key_line.setText("")
        self.value_line.setText("")
        self.scalar_line_1.setText("")
        self.scalar_line_2.setText("")
        self.answer_label.setText("")
        self.White()

    # define method for create button:
    def Create_Series(self):
        chosen = self.choose_box.currentText()
        if chosen == "with numpy array":
            High_number = self.range_line.text()
            size_number = self.size_line.text()
            if len(High_number) > 0 and len(size_number) > 0:
                High_number = int(High_number)
                size_number = int(size_number)
                local_array = np.random.randint(High_number, size = (size_number))
                self.global_series = pd.Series(local_array)
                self.df = pd.DataFrame(self.global_series)
                self.answer_label.setText("Series is created Successfully, from numpy array!")
                self.Green()
            else:
                self.answer_label.setText("Please Enter parameters for numpy array!")
                self.Red_1()
        
        elif chosen == "with list":
            numb = self.list_line.text()
            if len(numb) > 0:
                numb = int(numb)
                local_list = [i for i in range(1, numb + 1)]
                self.global_series = pd.Series(local_list)
                self.df = pd.DataFrame(self.global_series)
                self.answer_label.setText("Series is created Successfully, from list!")
                self.Green()
            else:
                self.answer_label.setText("Please Enter parameter for list!")
                self.Red_1()

        elif chosen == "with dictionary":
            keys = self.key_line.text()
            valuees = self.value_line.text()
            keys = keys.split(" ")
            valuees = valuees.split(" ")
            if len(keys) == len(valuees) and len(keys) >= 2 and len(valuees) >= 2:
                length = len(keys)
                local_dictionary = {}
                for i in range(length):
                    local_dictionary[keys[i]] = valuees[i]
                self.global_series = pd.Series(local_dictionary)
                self.df = pd.DataFrame(self.global_series)
                self.df.insert(loc=0, column = 'keys', value=keys)
                self.answer_label.setText("Series is created Successfully, from dictionary!")
                self.Green()
            else:
                self.answer_label.setText("Please define parameters CORRECTLY!")
                self.Red_1()
        
        elif chosen == "with scalar value":
            entered_value = self.scalar_line_1.text()
            entered_size = self.scalar_line_2.text()
            if len(entered_value) > 0 and len(entered_size) > 0:
                entered_value = int(entered_value)
                entered_size = int(entered_size)
                index_list = [i for i in range(entered_size)]
                self.global_series = pd.Series(entered_value, index = index_list)
                self.df = pd.DataFrame(self.global_series)
                self.answer_label.setText("Series is created Successfully, from scalar value!")
                self.Green()
            else:
                self.answer_label.setText("Please Enter parameter for scalar value!")
                self.Red_1()
        
        elif chosen == "with column from csv file":
            filename = self.filename_line.text()
            self.columnname = self.column_line.text()
            if len(filename) > 0 and len(self.columnname) > 0:
                try:
                    entered_file = pd.read_csv(f"{filename}")
                    try:
                        self.global_series = pd.Series(entered_file[f"{self.columnname}"])
                        self.df = pd.DataFrame(self.global_series)
                        self.answer_label.setText("Series is created Successfully, from CSV file!")
                        self.Green()
                    except KeyError:
                        self.answer_label.setText("Please Enter Column Name CORRECTLY!")
                        self.Red_1()
                except FileNotFoundError:
                    self.answer_label.setText("Please Enter File Name CORRECTLY!")
                    self.Red_1()
            else:
                self.answer_label.setText("Please Enter file and column names!")
                self.Red_1()
        
        self.display_button.setEnabled(True)

    # define method for display button:
    def Display_Series(self):
        chosen = self.choose_box.currentText()
        head = self.head_line.text()
        RowNumber = len(self.df.index)
        ColumnNumber = len(self.df.columns)

        self.table_widget.setColumnCount(ColumnNumber)
        self.table_widget.setRowCount(RowNumber)

        if chosen != "with dictionary":
            if chosen == "with column from csv file":
                self.table_widget.setHorizontalHeaderLabels([f"{self.columnname}"])
            else:
                self.table_widget.setHorizontalHeaderLabels([f"{head}"])
        else:
            self.table_widget.setHorizontalHeaderLabels(["1"])

        for rows in range(RowNumber):
            for columns in range(ColumnNumber):
                self.table_widget.setItem(rows, columns, QTableWidgetItem(str(self.df.iat[rows, columns])))
        
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()

        self.Clean_lines()
        self.display_button.setEnabled(False)

# ------------------------------------------- end --------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    water = Eminem()
    sys.exit(app.exec_())