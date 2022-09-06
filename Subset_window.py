from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFrame, QLineEdit, QComboBox, QTableWidget, QCheckBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QIntValidator
from PyQt5 import uic
import pandas as pd

class DoctorDre(QMainWindow):
    def __init__(self):
        super(DoctorDre, self).__init__()

        uic.loadUi("subset.ui", self)

        # define content:
        self.header_label = self.findChild(QLabel, "header_label")
        self.output_label = self.findChild(QLabel, "output_label")
        self.select_label = self.findChild(QLabel, "secret_label")
        self.file_label = self.findChild(QLabel, "file_label")
        self.column_label = self.findChild(QLabel, "column_label")
        self.result_label = self.findChild(QLabel, "result_label")
        self.warn_label = self.findChild(QLabel, "warn_label")
        self.filter_label = self.findChild(QLabel, "filter_label")
        self.determine_label = self.findChild(QLabel, "determine_label")
        self.row_label = self.findChild(QLabel, "row_label")
        self.boom_label = self.findChild(QLabel, "boom_label")
        self.null_label = self.findChild(QLabel, "null_label")

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")
        self.show_button = self.findChild(QPushButton, "show_button")
        self.filter_button = self.findChild(QPushButton, "filter_button")
        self.specific_button = self.findChild(QPushButton, "specific_button")
        self.distinct_button = self.findChild(QPushButton, "distinct_button")
        self.sort_button = self.findChild(QPushButton, "sort_button")

        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")
        self.line_3 = self.findChild(QFrame, "line_3")
        self.line_4 = self.findChild(QFrame, "line_4")
        self.line_5 = self.findChild(QFrame, "line_5")

        self.file_line = self.findChild(QLineEdit, "file_line")
        self.column_line = self.findChild(QLineEdit, "column_line")
        self.filter_line = self.findChild(QLineEdit, "filter_line")
        self.value_line = self.findChild(QLineEdit, "value_line")
        self.row_line_1 = self.findChild(QLineEdit, "row_line_1")
        self.row_line_2 = self.findChild(QLineEdit, "row_line_2")
        self.start_line_1 = self.findChild(QLineEdit, "start_line_1")
        self.start_line_2 = self.findChild(QLineEdit, "start_line_2")

        self.column_box = self.findChild(QComboBox, "column_box")
        self.filter_box = self.findChild(QComboBox, "filter_box")
        self.sort_box = self.findChild(QComboBox, "sort_box")

        self.yes_box = self.findChild(QCheckBox, "yes_box")
        self.no_box = self.findChild(QCheckBox, "no_box")

        self.table_widget = self.findChild(QTableWidget, "table_widget")

        # define place holders:
        self.file_line.setPlaceholderText("filename.csv")

        # set some buttons disabled:
        self.filter_button.setEnabled(False)
        self.specific_button.setEnabled(False)
        self.sort_button.setEnabled(False)
        self.distinct_button.setEnabled(False)

        # define int validator:
        Only_Int = QIntValidator()
        self.value_line.setValidator(Only_Int)
        self.row_line_1.setValidator(Only_Int)
        self.row_line_2.setValidator(Only_Int)
        self.start_line_1.setValidator(Only_Int)
        self.start_line_2.setValidator(Only_Int)

        # call defined methods from here:
        self.back_button.clicked.connect(self.GoBackToChoose)
        self.display_button.clicked.connect(self.Open_CSV)
        self.filter_button.clicked.connect(self.Filter_CSV)
        self.show_button.clicked.connect(self.Show_Columns)
        self.specific_button.clicked.connect(self.Select_Specific)
        self.sort_button.clicked.connect(self.Sort_Output)
        self.distinct_button.clicked.connect(self.Show_Distinct)

        self.show()

# ------------------------------------------ start -------------------------------------- #
    # define colors:
    def White(self):
        self.warn_label.setStyleSheet("background-color: rgb(240, 240, 240);")
    
    def Red(self):
        self.warn_label.setStyleSheet("background-color: rgb(255, 178, 216);")

    # define method for back button:
    def GoBackToChoose(self):
        from Choose_window import IceCube
        self.window_choose = QMainWindow()
        self.ice = IceCube()
        self.close()
    
    # define method for show button:
    def Show_Columns(self):
        filename = self.file_line.text()
        if len(filename) > 0:
            try:
                df = pd.read_csv(f'{filename}')
                Column_List = list(df.columns)
                self.result_label.setText(f'{Column_List}')
                self.warn_label.setText("")
                self.White()
            except FileNotFoundError:
                self.warn_label.setText("File does not exists, please enter valid file name!")
                self.Red()
        else:
            self.warn_label.setText("Please Enter File Name!")
            self.Red()
    
    # define method for display button:
    def Open_CSV(self):
        chosen = self.column_box.currentText()
        filename = self.file_line.text()
        if len(filename) > 0:
            try:
                self.df = pd.read_csv(f"{filename}")
                # add another method:
                self.Without_Nulls()

                if chosen == "Show Whole Table":
                    self.df = self.df
                elif chosen == "Show Part of the Table":
                    entered_columns = self.column_line.text()
                    column_list = entered_columns.split(" ")
                    self.df = self.df[column_list]

                row_number = len(self.df.index)
                column_number = len(self.df.columns)

                self.table_widget.setRowCount(row_number)
                self.table_widget.setColumnCount(column_number)
                self.table_widget.setHorizontalHeaderLabels(self.df.columns)

                for rows in range(row_number):
                    for columns in range(column_number):
                        self.table_widget.setItem(rows, columns, QTableWidgetItem(str(self.df.iat[rows, columns])))
                
                self.table_widget.resizeColumnsToContents()
                self.table_widget.resizeRowsToContents()
                self.warn_label.setText("")
                self.White()

            except FileNotFoundError:
                self.warn_label.setText("File does not exists, please enter valid file name!")
                self.Red()
        else:
            self.warn_label.setText("Please Enter File Name!")
            self.Red()

        self.filter_button.setEnabled(True)
        self.specific_button.setEnabled(True)
        self.sort_button.setEnabled(True)
        self.distinct_button.setEnabled(True)

    # define method for filter button:
    def Filter_CSV(self):
        column_name = self.filter_line.text()
        chosen_op = self.filter_box.currentText()

        if len(column_name) > 0 and len(self.value_line.text()) > 0:
            comparison_value = float(self.value_line.text())
            try:
                # add another method:
                self.Without_Nulls()
                if self.df[f"{column_name}"].dtypes in ('int64', 'float64'):
                    if chosen_op == "==":
                        filtered = self.df[self.df[f"{column_name}"] == comparison_value]
                    elif chosen_op == ">":
                        filtered = self.df[self.df[f"{column_name}"] > comparison_value]
                    elif chosen_op == "<":
                        filtered = self.df[self.df[f"{column_name}"] < comparison_value]
                    elif chosen_op == ">=":
                        filtered = self.df[self.df[f"{column_name}"] >= comparison_value]
                    elif chosen_op == "<=":
                        filtered = self.df[self.df[f"{column_name}"] <= comparison_value]

                    row_number = len(filtered.index)
                    column_number = len(filtered.columns)

                    self.table_widget.setRowCount(row_number)
                    self.table_widget.setColumnCount(column_number)
                    self.table_widget.setHorizontalHeaderLabels(filtered.columns)

                    for rows in range(row_number):
                        for columns in range(column_number):
                            self.table_widget.setItem(rows, columns, QTableWidgetItem(str(filtered.iat[rows, columns])))
                    
                    self.table_widget.resizeColumnsToContents()
                    self.table_widget.resizeRowsToContents()
                    self.warn_label.setText("")
                    self.White()
                else:
                    self.warn_label.setText("Column's data type should be int or float!")
                    self.Red()
            except KeyError:
                self.warn_label.setText("Column name is not correct!")
                self.Red()
        else:
            self.warn_label.setText("Please fill all labels!")
            self.Red()
    
    # determine method for specific button:
    def Select_Specific(self):
        filename = self.file_line.text()
        row_start = self.row_line_1.text()
        row_end = self.row_line_2.text()
        col_start = self.start_line_1.text()
        col_end = self.start_line_2.text()
        if len(filename) > 0 and len(row_start) > 0 and len(row_end) and len(col_start) > 0 and len(col_end) > 0:
            row_start = int(row_start) - 1
            row_end = int(row_end)
            col_start = int(col_start) - 1
            col_end = int(col_end)
            try:
                csv_file = pd.read_csv(f"{filename}")
                # add extra if statement:
                if self.yes_box.isChecked() == True and self.no_box.isChecked() != True:
                    for column in csv_file.columns:
                        csv_file = csv_file[csv_file[f"{column}"].notna()]
                else:
                    None
                #-------------------------#
                new_csv_file = csv_file.iloc[col_start:col_end, row_start:row_end]

                row_number = len(new_csv_file.index)
                col_number = len(new_csv_file.columns)

                self.table_widget.setRowCount(row_number)
                self.table_widget.setColumnCount(col_number)
                self.table_widget.setHorizontalHeaderLabels(new_csv_file.columns)

                for rows in range(row_number):
                    for col in range(col_number):
                        self.table_widget.setItem(rows, col, QTableWidgetItem(str(new_csv_file.iat[rows, col])))
                
                self.table_widget.resizeColumnsToContents()
                self.table_widget.resizeRowsToContents()
                self.warn_label.setText("")
                self.White()

            except FileNotFoundError:
                self.warn_label.setText("File does not exists, please enter valid file name!")
                self.Red()
        else:
            self.warn_label.setText("Please fill all labels!")
            self.Red()

    # determine method for without nulls choise:
    def Without_Nulls(self):
        if self.yes_box.isChecked() == True and self.no_box.isChecked() != True:
            for column in self.df.columns:
                self.df = self.df[self.df[f"{column}"].notna()]
        else:
            None
    
    # define method for sort button:
    def Sort_Output(self):
        chosen = self.sort_box.currentText()
        column_list = [i for i in self.df.columns]
        if chosen == "asc":
            answer = self.df.sort_values(by = [f"{column_list[0]}"])
        elif chosen == "desc":
            answer = self.df.sort_values(by = f"{column_list[0]}", ascending = False)
        
        row_num = len(answer.index)
        col_num = len(answer.columns)

        self.table_widget.setRowCount(row_num)
        self.table_widget.setColumnCount(col_num)
        self.table_widget.setHorizontalHeaderLabels(answer.columns)

        for r in range(row_num):
            for c in range(col_num):
                self.table_widget.setItem(r, c, QTableWidgetItem(str(answer.iat[r, c])))
        
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        self.warn_label.setText("")
        self.White()

    # define method for distinct button:
    def Show_Distinct(self):
        answer = self.df.drop_duplicates()
        row_num = len(answer.index)
        col_num = len(answer.columns)

        self.table_widget.setRowCount(row_num)
        self.table_widget.setColumnCount(col_num)
        self.table_widget.setHorizontalHeaderLabels(answer.columns)

        for r in range(row_num):
            for c in range(col_num):
                self.table_widget.setItem(r, c, QTableWidgetItem(str(answer.iat[r, c])))
        
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        self.warn_label.setText("")
        self.White()

# ------------------------------------------- end --------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    doctor = DoctorDre()
    sys.exit(app.exec_())