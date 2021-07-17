from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from PyQt5.uic import loadUiType

ui, _ = loadUiType('budgit.ui')

db = mysql.connector.connect(host="localhost", user="root", password="baryeh1122", database="company")
cur = db.cursor()


# Main class for application
class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.db = mysql.connector.connect(host="localhost", user="root", password="baryeh1122", database="company")
        self.cur = db.cursor()
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.HandleButtons()


    def Handle_UI_Changes(self):
        self.HideTheme()
        self.tabWidget.tabBar().setVisible(False)

    def HandleButtons(self):
        ##### hide and show themes #######
        self.pushButton_4.clicked.connect(self.ShowTheme)
        self.pushButton_10.clicked.connect(self.HideTheme)

        ##### move between pages buttons#####
        self.pushButton.clicked.connect(self.OpenPricesTab)
        self.pushButton_2.clicked.connect(self.OpenCompareTab)
        self.pushButton_3.clicked.connect(self.OpenSettingsTab)

        # ##### Clear button ##########
        #     self.pushButton_11.clicked.connect(self.ClearTable)

        ##### Search button ######
        self.pushButton_5.clicked.connect(self.SearchPrices)

        ##### Themes ######
        self.pushButton_6.clicked.connect(self.DarkTheme)
        self.pushButton_7.clicked.connect(self.DarkBlueTheme)
        self.pushButton_8.clicked.connect(self.DarkOrangeTheme)
        self.pushButton_9.clicked.connect(self.LightTheme)

    def ShowTheme(self):
        self.groupBox.show()

    def HideTheme(self):
        self.groupBox.hide()

    def ClearTable(self):
        self.tableWidget.clear()

    ################################
    ##### Opening pages/tabs #######

    def OpenPricesTab(self):
        self.tabWidget.setCurrentIndex(0)

    def OpenCompareTab(self):
        self.tabWidget.setCurrentIndex(1)

    def OpenSettingsTab(self):
        self.tabWidget.setCurrentIndex(2)

    ################################
    #####  Find Prices #######

    def SearchPrices(self):
        ProductName = self.lineEdit.text()

        query = ''' SELECT * FROM store WHERE product = %s'''
        self.cur.execute(query, ([ProductName]))
        data = self.cur.fetchall()
        print(data)

        self.tableWidget.setRowCount(0)
        for row, form in enumerate(data):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))

    ################################
    #####  UI Themes #######

    def DarkBlueTheme(self):
        style = open('Themes/darkblue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def DarkOrangeTheme(self):
        style = open('Themes/darkorange.css.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def DarkTheme(self):
        style = open('Themes/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def LightTheme(self):
        style = open('Themes/qlight.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
