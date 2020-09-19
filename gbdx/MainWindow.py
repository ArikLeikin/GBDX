# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gbdxtools import Interface
from gbdxtools.catalog import Catalog
from gbdxtools.images.catalog_image import CatalogImage
import time
import threading

gbdx = Interface()


class Ui_MainWindow(object):
    imageName = "C:\\Users\\vpadmin.VIDEOINFORM\\Downloads\\output.tif"
    catId = []
    submitted = 0
    crop = None

    def polygonBuilder(self, pointNumber):# Example "POLYGON((56.335213571289046 25.217757840251576,56.335385232666 25.176906771954453,56.36611261914061 25.17628535715365,56.36559763500975 25.21806844224977,56.335213571289046 25.217757840251576))"
        point1 = self.Point1Entry.toPlainText()
        point2 = self.Point2Entry.toPlainText()
        point3 = self.Point3Entry.toPlainText()
        point4 = self.Point4Entry.toPlainText()
        self.crop = "Polygon ((" + point1 + "," + point2 + "," + point3 + "," + point4 + "," + point1 + "))"
        print(self.crop)

    def imageNameBuilder(self):
        self.imageName = "C:\\Users\\vpadmin.VIDEOINFORM\\PycharmProjects\\gbdx\\Images\\" + self.ImageNameEntry.text() + ".tif"
        print(self.imageName)

    def imageDownload(self):
        if self.submitted == 1:

            id = self.catId
            c = CatalogImage(id[0], pansharpen=True, acomp=True)
            print(time.strftime("%H:%M:%S") + "Download Started")
            aoi = c.aoi(wkt=self.crop)
            print("crop done")
            image = aoi.geotiff(path=self.imageName)
            print("aoi.geotiff done")

    def imageDownloadThread(self):
        threading.Thread(target=self.imageDownload).start()

    def orderImage(self):
        order_id = gbdx.ordering.order(self.catId)
        print(order_id)
        self.CatIDsShow.append("Order Submitted - " + order_id)
        self.submitted = 1

    def orderImageThread(self):
        threading.Thread(target=self.orderImage).start()

    def submitCatID(self):
        input = self.EntryCatID.text()
        if len(input) == 16:
            self.catId.append(self.EntryCatID.text())
            print(self.catId)
            self.CatIDsShow.append(str(self.catId))
        else:
            self.CatIDsShow.append("Incorrect catalog ID")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 635)

    # Main Tab Block
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 621))
        self.tabWidget.setMinimumSize(QtCore.QSize(861, 621))
        self.tabWidget.setMaximumSize(QtCore.QSize(861, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.Main_Tab = QtWidgets.QWidget()
        self.Main_Tab.setObjectName("Main_Tab")
        self.MainPageTitle = QtWidgets.QTextEdit(self.Main_Tab)
        self.MainPageTitle.setGeometry(QtCore.QRect(210, 10, 421, 51))
        self.MainPageTitle.setObjectName("MainPageTitle")
        self.WorkflowImage = QtWidgets.QLabel(self.Main_Tab)
        self.WorkflowImage.setGeometry(QtCore.QRect(0, 100, 851, 501))
        self.WorkflowImage.setText("")
        self.WorkflowImage.setPixmap(QtGui.QPixmap("../../Desktop/Capture11.PNG"))
        self.WorkflowImage.setObjectName("WorkflowImage")
        self.tabWidget.addTab(self.Main_Tab, "")

    # Order Image Tab block
        self.Order_Image = QtWidgets.QWidget()
        self.Order_Image.setObjectName("Order_Image")

        # Enter CatID Label
        self.EnterCatID_Label = QtWidgets.QLabel(self.Order_Image)
        self.EnterCatID_Label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.EnterCatID_Label.setObjectName("EnterCatID_Label")

        # Entry Line
        self.EntryCatID = QtWidgets.QLineEdit(self.Order_Image)
        self.EntryCatID.setGeometry(QtCore.QRect(110, 20, 141, 20))
        self.EntryCatID.setObjectName("EntryCatID")

        # Dialog Box
        self.CatIDsShow = QtWidgets.QTextBrowser(self.Order_Image)
        self.CatIDsShow.setGeometry(QtCore.QRect(20, 50, 231, 192))
        self.CatIDsShow.setObjectName("CatIDsShow")

        # Submit Button
        self.CatID_SubmitButton = QtWidgets.QPushButton(self.Order_Image)
        self.CatID_SubmitButton.clicked.connect(self.submitCatID)
        self.CatID_SubmitButton.setGeometry(QtCore.QRect(260, 20, 75, 21))
        self.CatID_SubmitButton.setObjectName("CatID_SubmitButton")

        # Order Button
        self.OrderButton = QtWidgets.QPushButton(self.Order_Image)
        self.OrderButton.clicked.connect(self.orderImageThread)
        self.OrderButton.setGeometry(QtCore.QRect(320, 520, 171, 41))
        self.OrderButton.setObjectName("OrderButton")
        self.tabWidget.addTab(self.Order_Image, "")

    # Download Image tab
        self.Download_Tab = QtWidgets.QWidget()
        self.Download_Tab.setObjectName("Download_Tab")

        # Enter Coordinates Label
        self.EnterPolygonCoordinatesLabel = QtWidgets.QLabel(self.Download_Tab)
        self.EnterPolygonCoordinatesLabel.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.EnterPolygonCoordinatesLabel.setObjectName("EnterPolygonCoordinatesLabel")

        # Point 1
        self.Point1Label = QtWidgets.QLabel(self.Download_Tab)
        self.Point1Label.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.Point1Label.setObjectName("Point1Label")
        self.Point1Entry = QtWidgets.QTextEdit(self.Download_Tab)
        self.Point1Entry.setGeometry(QtCore.QRect(10, 60, 121, 31))
        self.Point1Entry.setObjectName("Point1Entry")
        # Point 2
        self.Point2Label = QtWidgets.QLabel(self.Download_Tab)
        self.Point2Label.setGeometry(QtCore.QRect(140, 40, 47, 13))
        self.Point2Label.setObjectName("Point2Label")
        self.Point2Entry = QtWidgets.QTextEdit(self.Download_Tab)
        self.Point2Entry.setGeometry(QtCore.QRect(140, 60, 121, 31))
        self.Point2Entry.setObjectName("Point2Entry")
        # Point 3
        self.Point3Label = QtWidgets.QLabel(self.Download_Tab)
        self.Point3Label.setGeometry(QtCore.QRect(270, 40, 47, 13))
        self.Point3Label.setObjectName("Point3Label")
        self.Point3Entry = QtWidgets.QTextEdit(self.Download_Tab)
        self.Point3Entry.setGeometry(QtCore.QRect(270, 60, 121, 31))
        self.Point3Entry.setObjectName("Point3Entry")
        # Point 4
        self.Point4Label = QtWidgets.QLabel(self.Download_Tab)
        self.Point4Label.setGeometry(QtCore.QRect(400, 40, 47, 13))
        self.Point4Label.setObjectName("Point4Label")
        self.Point4Entry = QtWidgets.QTextEdit(self.Download_Tab)
        self.Point4Entry.setGeometry(QtCore.QRect(400, 60, 121, 31))
        self.Point4Entry.setObjectName("Point4Entry")
        # Submit Coordinates Button
        self.SubmitCoordinates = QtWidgets.QPushButton(self.Download_Tab)
        self.SubmitCoordinates.setGeometry(QtCore.QRect(530, 60, 75, 31))
        self.SubmitCoordinates.setObjectName("SubmitCoordinates")
        self.SubmitCoordinates.clicked.connect(self.polygonBuilder)

        # Enter Image Name
        self.EnterImageNameLabel = QtWidgets.QLabel(self.Download_Tab)
        self.EnterImageNameLabel.setGeometry(QtCore.QRect(10, 120, 101, 21))
        self.EnterImageNameLabel.setObjectName("EnterImageNameLabel")
        self.ImageNameEntry = QtWidgets.QLineEdit(self.Download_Tab)
        self.ImageNameEntry.setGeometry(QtCore.QRect(10, 140, 201, 21))
        self.ImageNameEntry.setObjectName("ImageNameEntry")
        self.SubmitImageName = QtWidgets.QPushButton(self.Download_Tab)
        self.SubmitImageName.setGeometry(QtCore.QRect(220, 140, 75, 21))
        self.SubmitImageName.setObjectName("SubmitImageName")
        self.SubmitImageName.clicked.connect(self.imageNameBuilder)

        # File Location
        self.SelectFileLocationLabel = QtWidgets.QLabel(self.Download_Tab)
        self.SelectFileLocationLabel.setGeometry(QtCore.QRect(10, 190, 121, 16))
        self.SelectFileLocationLabel.setObjectName("SelectFileLocationLabel")

        # Download Button
        self.DownloadImageButton = QtWidgets.QPushButton(self.Download_Tab)
        self.DownloadImageButton.setGeometry(QtCore.QRect(320, 520, 171, 41))
        self.DownloadImageButton.setObjectName("DownloadImageButton")
        self.DownloadImageButton.clicked.connect(self.imageDownloadThread)

        self.tabWidget.addTab(self.Download_Tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("GBDX Image Downloader", "GBDX Image Downloader"))
        self.MainPageTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">GBDX Images Downloader </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main_Tab), _translate("MainWindow", "Main"))
        self.EnterCatID_Label.setText(_translate("MainWindow", "Enter Catalog ID:"))
        self.CatID_SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.OrderButton.setText(_translate("MainWindow", "Order"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Order_Image), _translate("MainWindow", "Order Image"))
        self.EnterPolygonCoordinatesLabel.setText(_translate("MainWindow", "Enter Polygon Coordinates:"))
        self.Point1Label.setText(_translate("MainWindow", "Point 1"))
        self.Point2Label.setText(_translate("MainWindow", "Point 2"))
        self.Point3Label.setText(_translate("MainWindow", "Point 3"))
        self.Point4Label.setText(_translate("MainWindow", "Point 4"))
        self.EnterImageNameLabel.setText(_translate("MainWindow", "Enter Image Name"))
        self.SubmitImageName.setText(_translate("MainWindow", "Submit"))
        self.SelectFileLocationLabel.setText(_translate("MainWindow", "Select File Location"))
        self.DownloadImageButton.setText(_translate("MainWindow", "Download Image"))
        self.SubmitCoordinates.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Download_Tab), _translate("MainWindow", "Download Image"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())