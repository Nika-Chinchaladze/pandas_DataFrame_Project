from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit, QComboBox, QCheckBox, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import uic
import pandas as pd

class RandyOrton(QMainWindow):
    def __init__(self):
        super(RandyOrton, self).__init__()

        uic.loadUi("text.ui", self)

        # define content:
        self.head_label = self.findChild(QLabel, "head_label")
        self.output_label = self.findChild(QLabel, "output_label")
        self.manipulate_label = self.findChild(QLabel, "manipulate_label")
        self.case_label = self.findChild(QLabel, "case_label")
        self.split_label = self.findChild(QLabel, "split_label")
        self.find_label = self.findChild(QLabel, "find_label")
        self.extreme_label = self.findChild(QLabel, "extreme_label")
        self.replace_label = self.findChild(QLabel, "replace_label")
        self.choose_label = self.findChild(QLabel, "choose_label")
        self.warn_label = self.findChild(QLabel, "warn_label")

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")

        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.line_3 = self.findChild(QFrame, "line_3")
        self.line_4 = self.findChild(QFrame, "line_4")
        self.line_5 = self.findChild(QFrame, "line_5")
        self.line_6 = self.findChild(QFrame, "line_6")
        self.line_7 = self.findChild(QFrame, "line_7")
        self.line_8 = self.findChild(QFrame, "line_8")

        self.column_line = self.findChild(QLineEdit, "column_line")
        self.split_line = self.findChild(QLineEdit, "split_line")
        self.find_line = self.findChild(QLineEdit, "find_line")
        self.value_line = self.findChild(QLineEdit, "value_line")
        self.extreme_line = self.findChild(QLineEdit, "extreme_line")
        self.r_line_1 = self.findChild(QLineEdit, "r_line_1")
        self.r_line_2 = self.findChild(QLineEdit, "r_line_2")
        self.r_line_3 = self.findChild(QLineEdit, "r_line_3")
        self.file_line = self.findChild(QLineEdit, "file_line")
        self.case_line = self.findChild(QLineEdit, "case_line")

        self.case_box = self.findChild(QComboBox, "case_box")
        self.extreme_box = self.findChild(QComboBox, "extreme_box")
        self.table_widget = self.findChild(QTableWidget, "table_widget")

        self.check_letters = self.findChild(QCheckBox, "check_letters")
        self.check_split = self.findChild(QCheckBox, "check_split")
        self.check_find = self.findChild(QCheckBox, "check_find")
        self.check_extreme = self.findChild(QCheckBox, "check_extreme")
        self.check_replace = self.findChild(QCheckBox, "check_replace")

        # define some place holders:
        self.file_line.setPlaceholderText("name.csv")
        self.column_line.setPlaceholderText("column")
        self.find_line.setPlaceholderText("column")
        self.extreme_line.setPlaceholderText("column")
        self.r_line_1.setPlaceholderText("column")
        self.r_line_2.setPlaceholderText("what")
        self.r_line_3.setPlaceholderText("with")
        self.split_line.setPlaceholderText("how")
        self.value_line.setPlaceholderText("value")
        self.case_line.setPlaceholderText("column")

        # call defined methods from here:
        self.back_button.clicked.connect(self.Return_Back_To_Choose)
        self.display_button.clicked.connect(self.Display_CSV)


        self.show()

# ------------------------------------------ start -------------------------------------- #
    # define some colors:
    def White(self):
        self.warn_label.setStyleSheet("background-color: rgb(240, 240, 240);")
    
    def Red(self):
        self.warn_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define method for back button:
    def Return_Back_To_Choose(self):
        from Choose_window import IceCube
        self.window_choose = QMainWindow()
        self.ice = IceCube()
        self.close()
    
    # define method for display_button:
    def Display_CSV(self):
        filename = self.file_line.text()
        if len(filename) > 0:
            try:
                self.inseption = pd.read_csv(f"{filename}")

                # LowerCase or UpperCase:
                if self.check_letters.isChecked() == True:
                    column_name = self.case_line.text()
                    case_type = self.case_box.currentText()
                    if len(column_name) > 0:
                        try:
                            if self.inseption[f"{column_name}"].dtypes == "object":
                                if case_type == "LowerCase":
                                    self.df = self.inseption[f"{column_name}"].str.lower()
                                    self.df = pd.DataFrame(self.df)
                                elif case_type == "UpperCase":
                                    self.df = self.inseption[f"{column_name}"].str.upper()
                                    self.df = pd.DataFrame(self.df)
                            else:
                                None
                        except KeyError:
                            None
                    else:
                        None
                
                
                # Split Column into two column:
                elif self.check_split.isChecked() == True:
                    split_name = self.column_line.text()
                    if len(split_name) > 0:
                        first = pd.DataFrame()
                        try:
                            first['First Name'] = self.df[f"{split_name}"].str.split(" ").str.get(0)
                            first['Last Name'] = self.df[f"{split_name}"].str.split(" ").str.get(1)
                            self.df = first
                        except KeyError:
                            None 
                    else:
                        None
                
                
                # Find Value in the column:
                elif self.check_find.isChecked() == True:
                    find_name = self.find_line.text()
                    value_name = self.value_line.text()
                    if len(find_name) > 0 and len(value_name) > 0:
                        try:
                            second = self.df[self.df[f"{find_name}"].str.contains(f"{value_name}")]
                            self.df = second
                        except KeyError:
                            None
                    else:
                        None
                
                
                # find extreme values:
                elif self.check_extreme.isChecked() == True:
                    ext_name = self.extreme_line.text()
                    ext_type = self.extreme_box.currentText()
                    if len(ext_name) > 0:
                        try:
                            if ext_type == "with Max length":
                                third = self.df.loc[self.df[f"{ext_name}"].str.len().idxmax(), f"{ext_name}"]
                                boom = pd.Series([f"{third}"])
                                self.df = pd.DataFrame()
                                self.df['Value with Max length'] = boom
                            elif ext_type == "with Min length":
                                third = self.df.loc[self.df[f"{ext_name}"].str.len().idxmin(), f"{ext_name}"]
                                boom = pd.Series([f"{third}"])
                                self.df = pd.DataFrame()
                                self.df['Value with Min length'] = boom
                        except KeyError:
                            None
                    else:
                        None
                
                # replace values:
                elif self.check_replace.isChecked() == True:
                    replace_name = self.r_line_1.text()
                    from_val = self.r_line_2.text()
                    to_val = self.r_line_3.text()
                    if len(replace_name) > 0 and len(from_val) > 0 and len(to_val) > 0:
                        try:
                            self.df[f"{replace_name}"] = self.df[f"{replace_name}"].replace({f"{from_val}":f"{to_val}"})
                        except KeyError:
                            None
                    else:
                        None

                # last part of conditional statement:
                else:
                    self.df = self.inseption

                # self.df visualization part:
                row_num = len(self.df.index)
                col_num = len(self.df.columns)

                self.table_widget.setRowCount(row_num)
                self.table_widget.setColumnCount(col_num)
                self.table_widget.setHorizontalHeaderLabels(self.df.columns)

                for rows in range(row_num):
                    for columns in range(col_num):
                        self.table_widget.setItem(rows, columns, QTableWidgetItem(str(self.df.iat[rows, columns])))
                
                self.table_widget.resizeColumnsToContents()
                self.table_widget.resizeRowsToContents()
                self.warn_label.setText("")
                self.White()
            except FileNotFoundError:
                self.warn_label.setText("Please enter valid file name, this file does not exists!")
                self.Red()    
        else:
            self.warn_label.setText("Please enter file name!")
            self.Red()
        
        self.df = self.inseption

# ------------------------------------------- end --------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    randy = RandyOrton()
    sys.exit(app.exec_())