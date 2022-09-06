from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import pandas as pd

class SnoopDog(QMainWindow):
    def __init__(self):
        super(SnoopDog, self).__init__()

        uic.loadUi("statistics.ui", self)

        # define content:
        self.head_label = self.findChild(QLabel, "head_label")
        self.input_label = self.findChild(QLabel, "input_label")
        self.calculate_label = self.findChild(QLabel, "calculate_label")
        self.choose_label = self.findChild(QLabel, "choose_label")
        self.file_label = self.findChild(QLabel, "file_label")
        self.column_label = self.findChild(QLabel, "column_label")
        self.result_label = self.findChild(QLabel, "result_label")
        self.answer_label = self.findChild(QLabel, "answer_label")
        self.direct_label = self.findChild(QLabel, "direct_label")
        self.warning_label = self.findChild(QLabel, "warning_label")

        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.line_3 = self.findChild(QFrame, "line_3")

        self.open_button = self.findChild(QPushButton, "open_button")
        self.back_button = self.findChild(QPushButton, "back_button")
        self.find_button = self.findChild(QPushButton, "find_button")

        self.file_line = self.findChild(QLineEdit, "file_line")
        self.column_line = self.findChild(QLineEdit, "column_line")
        self.choose_box = self.findChild(QComboBox, "choose_box")
        self.table_widget = self.findChild(QTableWidget, "table_widget")

        # define place holders:
        self.file_line.setPlaceholderText("filename.csv")
        self.column_line.setPlaceholderText("column name")

        # call defined method from here:
        self.back_button.clicked.connect(self.ReturnBack)
        self.open_button.clicked.connect(self.Open_CSV)
        self.find_button.clicked.connect(self.Calculate_Statistics)

        self.show()

# ------------------------------------------ start -------------------------------------- #
    # define colors:
    def Green(self):
        self.warning_label.setStyleSheet("background-color: rgb(155, 255, 184);")

    def White(self):
        self.warning_label.setStyleSheet("background-color: rgb(240, 240, 240);")
    
    def Red(self):
        self.warning_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define button for back button:
    def ReturnBack(self):
        from Choose_window import IceCube
        self.window_first = QMainWindow()
        self.ice = IceCube()
        self.close()
    
    # define method for open button:
    def Open_CSV(self):
        file_name = self.file_line.text()
        if len(file_name) > 0:
            try:
                self.df = pd.read_csv(f"{file_name}")

                RowNumber = len(self.df.index)
                ColumnNumber = len(self.df.columns)

                self.table_widget.setColumnCount(ColumnNumber)
                self.table_widget.setRowCount(RowNumber)
                self.table_widget.setHorizontalHeaderLabels(self.df.columns)
                

                for rows in range(RowNumber):
                    for columns in range(ColumnNumber):
                        self.table_widget.setItem(rows, columns, QTableWidgetItem(str(self.df.iat[rows, columns])))
                
                self.table_widget.resizeColumnsToContents()
                self.table_widget.resizeRowsToContents()
                self.warning_label.setText("")
                self.White()
            except FileNotFoundError:
                self.warning_label.setText("File does not EXISTS!")
                self.Red()
        else:
            self.warning_label.setText("Please enter File name!")
            self.Red()

    # define method for find button:
    def Calculate_Statistics(self):
        chosen = self.choose_box.currentText()
        file_name = self.file_line.text()
        column_name = self.column_line.text()

        if len(file_name) > 0 and len(column_name) > 0:
            try:
                self.csv = pd.read_csv(f"{file_name}")
                try:
                    if chosen == "mean":
                        if self.csv[f"{column_name}"].dtypes in ('int64', 'float64'):
                            answer = round(self.csv[f"{column_name}"].mean(), 2)
                            self.answer_label.setText(f"{answer}")
                            self.direct_label.setText(f"mean of {column_name}:")
                            self.warning_label.setText("")
                            self.White()
                        else:
                            self.warning_label.setText("Type of Column must be int or float!")
                            self.Red()
                    
                    elif chosen == "median":
                        if self.csv[f"{column_name}"].dtypes in ('int64', 'float64'):
                            answer = self.csv[f"{column_name}"].median()
                            self.answer_label.setText(f"{answer}")
                            self.direct_label.setText(f"median of {column_name}:")
                            self.warning_label.setText("")
                            self.White()
                        else:
                            self.warning_label.setText("Type of Column must be int or float!")
                            self.Red()
                    
                    elif chosen == "min":
                        if self.csv[f"{column_name}"].dtypes in ('int64', 'float64'):
                            answer = self.csv[f"{column_name}"].min()
                            self.answer_label.setText(f"{answer}")
                            self.direct_label.setText(f"minimum number in {column_name}:")
                            self.warning_label.setText("")
                            self.White()
                        else:
                            self.warning_label.setText("Type of Column must be int or float!")
                            self.Red()
                    
                    elif chosen == "max":
                        if self.csv[f"{column_name}"].dtypes in ('int64', 'float64'):
                            answer = self.csv[f"{column_name}"].max()
                            self.answer_label.setText(f"{answer}")
                            self.direct_label.setText(f"maximum number in {column_name}:")
                            self.warning_label.setText("")
                            self.White()
                        else:
                            self.warning_label.setText("Type of Column must be int or float!")
                            self.Red()
                    
                    elif chosen == "skew":
                        if self.csv[f"{column_name}"].dtypes in ('int64', 'float64'):
                            answer = round(self.csv[f"{column_name}"].skew(), 2)
                            self.answer_label.setText(f"{answer}")
                            self.direct_label.setText(f"Asymmetry of distribution in {column_name}:")
                            self.warning_label.setText("")
                            self.White()
                        else:
                            self.warning_label.setText("Type of Column must be int or float!")
                            self.Red()
                    
                    elif chosen == "std":
                        if self.csv[f"{column_name}"].dtypes in ('int64', 'float64'):
                            answer = round(self.csv[f"{column_name}"].std(), 2)
                            self.answer_label.setText(f"{answer}")
                            self.direct_label.setText(f"Stardard Deviation of {column_name}:")
                            self.warning_label.setText("")
                            self.White()
                        else:
                            self.warning_label.setText("Type of Column must be int or float!")
                            self.Red()
                    
                    elif chosen == "count":
                        answer = self.csv[f"{column_name}"].count()
                        self.answer_label.setText(f"{answer}")
                        self.direct_label.setText(f"Number of records in {column_name}:")
                        self.warning_label.setText("")
                        self.White()
                    
                    elif chosen == "value_counts":
                        answer = str(self.csv[f"{column_name}"].value_counts())
                        name_pos = answer.find('Name')
                        answer = answer[0:name_pos]
                        self.answer_label.setText(f"{answer}")
                        self.direct_label.setText(f"Number of DISTINCT elements in {column_name}:")
                        self.warning_label.setText("")
                        self.White()
                        
                except KeyError:
                    self.warning_label.setText("Column Name Is NOT CORRECT!")
                    self.Red()
            except FileNotFoundError:
                self.warning_label.setText("File Does not EXISTS!")
                self.Red()    
        else:
            self.warning_label.setText("Please Fill File and Column Name Fields!")
            self.Red()

# ------------------------------------------- end --------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dog = SnoopDog()
    sys.exit(app.exec_())