from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from functools import partial
from FileManager import FileManager
from Graph import Graph
from BFSAlgo import BFSAlgo
import os
import networkx as nx

import matplotlib.pyplot as plt
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_GraphBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GraphBrowse.setGeometry(QtCore.QRect(650, 90, 75, 23))
        self.pushButton_GraphBrowse.setObjectName("GraphBrowse")
        self.plainTextEdit_HospitalFileURL = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit_HospitalFileURL.setGeometry(QtCore.QRect(170, 190, 441, 41))
        self.plainTextEdit_HospitalFileURL.setObjectName("plainTextEdit_HospitalFileURL")
        self.pushButton_HospitalBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_HospitalBrowse.setGeometry(QtCore.QRect(650, 200, 75, 23))
        self.pushButton_HospitalBrowse.setObjectName("HospitalBrowse")
        self.label_Hospital = QtWidgets.QLabel(self.centralwidget)
        self.label_Hospital.setGeometry(QtCore.QRect(170, 170, 47, 13))
        self.label_Hospital.setObjectName("label_Hospital")
        self.label_Graph = QtWidgets.QLabel(self.centralwidget)
        self.label_Graph.setGeometry(QtCore.QRect(170, 60, 47, 13))
        self.label_Graph.setObjectName("label_Graph")
        self.plainTextEdit_GraphFileURL = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit_GraphFileURL.setGeometry(QtCore.QRect(170, 80, 441, 41))
        self.plainTextEdit_GraphFileURL.setObjectName("plainTextEdit_GraphFileURL")
        self.pushButton_Top1Hospital = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Top1Hospital.setGeometry(QtCore.QRect(90, 310, 101, 23))
        self.pushButton_Top1Hospital.setObjectName("pushButton_Top1Hospital")
        self.pushButton_Top2Hospital = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Top2Hospital.setGeometry(QtCore.QRect(350, 310, 101, 23))
        self.pushButton_Top2Hospital.setObjectName("pushButton_Top2Hospital")
        self.pushButton_TopKHospital = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_TopKHospital.setGeometry(QtCore.QRect(610, 310, 101, 23))
        self.pushButton_TopKHospital.setObjectName("pushButton_TopKHospital")
        self.pushButton_AutoGraphGenerator = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AutoGraphGenerator.setGeometry(QtCore.QRect(220, 50, 91, 23))
        self.pushButton_AutoGraphGenerator.setObjectName("pushButton_AutoGraphGenerator")
        # self.pushButton_AutoHospitalGenerator = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_AutoHospitalGenerator.setGeometry(QtCore.QRect(220, 160, 91, 23))
        # self.pushButton_AutoHospitalGenerator.setObjectName("pushButton_AutoHospitalGenerator")
        self.pushButton_ClearOutput = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ClearOutput.setGeometry(QtCore.QRect(670, 570, 101, 23))
        self.pushButton_ClearOutput.setObjectName("pushButton_ClearOutput")
        self.spinBox_Kvalue = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Kvalue.setGeometry(QtCore.QRect(650, 270, 51, 31))
        self.spinBox_Kvalue.setMinimum(3)
        self.spinBox_Kvalue.setObjectName("spinBox_Kvalue")
        self.spinBox_Kvalue.valueChanged.connect(self.getSpinBoxValue)
        self.spinBox_value = self.spinBox_Kvalue.value()
        self.label_Kvalue = QtWidgets.QLabel(self.centralwidget)
        self.label_Kvalue.setGeometry(QtCore.QRect(620, 280, 47, 13))
        self.label_Kvalue.setObjectName("label_Kvalue")
        self.plainTextEdit_Output = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit_Output.setGeometry(QtCore.QRect(30, 360, 741, 201))
        self.plainTextEdit_Output.setObjectName("plainTextEdit_Output")
        self.label_Output = QtWidgets.QLabel(self.centralwidget)
        self.label_Output.setGeometry(QtCore.QRect(30, 340, 47, 13))
        self.label_Output.setObjectName("label_Output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_GraphBrowse.setText(_translate("MainWindow", "Browse"))
        self.pushButton_HospitalBrowse.setText(_translate("MainWindow", "Browse"))
        self.label_Hospital.setText(_translate("MainWindow", "Hospital"))
        self.label_Graph.setText(_translate("MainWindow", "Graph"))
        self.pushButton_Top1Hospital.setText(_translate("MainWindow", "Top 1 Hospital"))
        self.pushButton_Top2Hospital.setText(_translate("MainWindow", "Top 2 Hospital"))
        self.pushButton_TopKHospital.setText(_translate("MainWindow", "Top K Hospital"))
        self.pushButton_AutoGraphGenerator.setText(_translate("MainWindow", "Auto generator"))
        #self.pushButton_AutoHospitalGenerator.setText(_translate("MainWindow", "Auto generator"))
        self.label_Kvalue.setText(_translate("MainWindow", "K ="))
        self.label_Output.setText(_translate("MainWindow", "Output"))
        self.pushButton_ClearOutput.setText(_translate("MainWindow", "Clear"))

        # readin txt file
        self.pushButton_GraphBrowse.clicked.connect(partial(self.browseButtonOnClick, self.pushButton_GraphBrowse.objectName()))
        self.pushButton_HospitalBrowse.clicked.connect(partial(self.browseButtonOnClick, self.pushButton_HospitalBrowse.objectName()))

        # search k noOfHospitals
        self.pushButton_Top1Hospital.clicked.connect(partial(self.searchButtonOnClick, 1))
        self.pushButton_Top2Hospital.clicked.connect(partial(self.searchButtonOnClick, 2))
        self.pushButton_TopKHospital.clicked.connect(partial(self.searchButtonOnClick, 0))

        # clear
        self.pushButton_ClearOutput.clicked.connect(self.ClearOnClick)

        # auto graph generator
        self.pushButton_AutoGraphGenerator.clicked.connect(self.autoGraphGenerator)

    def open_dialog(self, name):
        try:
            filename = QFileDialog.getOpenFileName()
            if name == self.pushButton_GraphBrowse.objectName():
                self.plainTextEdit_GraphFileURL.setText(filename[0])
            elif name == self.pushButton_HospitalBrowse.objectName():
                self.plainTextEdit_HospitalFileURL.setText(filename[0])
        except Exception as e:
            print(e)

    def browseButtonOnClick(self, name):
        try:
            self.open_dialog(name)
            if name == self.pushButton_GraphBrowse.objectName():
                self.plainTextEdit_GraphFileURL.setText(self.plainTextEdit_GraphFileURL.toPlainText())
            elif name == self.pushButton_HospitalBrowse.objectName():
                self.plainTextEdit_HospitalFileURL.setText(self.plainTextEdit_HospitalFileURL.toPlainText())
        except Exception as e:
            print(e)

    def searchButtonOnClick(self, noOfHospital):
        try:
            graphDirectory = self.plainTextEdit_GraphFileURL.toPlainText()
            graphList = FileManager.readfile(graphDirectory)

            if noOfHospital == 0:
                noOfHospital = self.spinBox_value

            output = BFSAlgo.search(self.plainTextEdit_GraphFileURL.toPlainText(), self.plainTextEdit_HospitalFileURL.toPlainText(), "Path To Nearby Hospital.txt", noOfHospital)
            self.plainTextEdit_Output.append(output)

            G = Graph(graphList)
            G.drawGraph()
        except Exception as e:
            print(e)

    def ClearOnClick(self):
        self.plainTextEdit_Output.clear()

    def getSpinBoxValue(self):
        # getting current value
        self.spinBox_value = self.spinBox_Kvalue.value()

    def autoGraphGenerator(self):
        G = Graph(0, True, 50, 0.04, 'SampleGraph_AutoGenerated.txt')
        self.plainTextEdit_GraphFileURL.setText(str(os.getcwd().replace('\\', '/')) + '/SampleGraph_AutoGenerated.txt')
        G.drawGraph()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
