# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1128, 693)
        MainWindow.setStyleSheet("font: 14pt \"Agency FB\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 92, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.StartProcess = QtWidgets.QPushButton(self.centralwidget)
        self.StartProcess.setGeometry(QtCore.QRect(440, 360, 231, 51))
        self.StartProcess.setObjectName("StartProcess")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 270, 671, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.NameMatching_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.NameMatching_lineEdit.setObjectName("NameMatching_lineEdit")
        self.horizontalLayout_5.addWidget(self.NameMatching_lineEdit)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 1091, 39))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.VideoPath_lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoPath_lineEdit.sizePolicy().hasHeightForWidth())
        self.VideoPath_lineEdit.setSizePolicy(sizePolicy)
        self.VideoPath_lineEdit.setFrame(True)
        self.VideoPath_lineEdit.setObjectName("VideoPath_lineEdit")
        self.horizontalLayout_2.addWidget(self.VideoPath_lineEdit)
        self.ChooseVIdeoPath_pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChooseVIdeoPath_pushButton.sizePolicy().hasHeightForWidth())
        self.ChooseVIdeoPath_pushButton.setSizePolicy(sizePolicy)
        self.ChooseVIdeoPath_pushButton.setObjectName("ChooseVIdeoPath_pushButton")
        self.horizontalLayout_2.addWidget(self.ChooseVIdeoPath_pushButton)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 70, 1091, 39))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.SubtitlePath_lineEdit = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubtitlePath_lineEdit.sizePolicy().hasHeightForWidth())
        self.SubtitlePath_lineEdit.setSizePolicy(sizePolicy)
        self.SubtitlePath_lineEdit.setFrame(True)
        self.SubtitlePath_lineEdit.setObjectName("SubtitlePath_lineEdit")
        self.horizontalLayout.addWidget(self.SubtitlePath_lineEdit)
        self.ChooseSubtitlePath_pushButton = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChooseSubtitlePath_pushButton.sizePolicy().hasHeightForWidth())
        self.ChooseSubtitlePath_pushButton.setSizePolicy(sizePolicy)
        self.ChooseSubtitlePath_pushButton.setObjectName("ChooseSubtitlePath_pushButton")
        self.horizontalLayout.addWidget(self.ChooseSubtitlePath_pushButton)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 190, 671, 61))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.NewName_lineEdit = QtWidgets.QLineEdit(self.widget2)
        self.NewName_lineEdit.setObjectName("NewName_lineEdit")
        self.horizontalLayout_4.addWidget(self.NewName_lineEdit)
        self.ChooseLanguage_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ChooseLanguage_comboBox.setGeometry(QtCore.QRect(150, 130, 111, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChooseLanguage_comboBox.sizePolicy().hasHeightForWidth())
        self.ChooseLanguage_comboBox.setSizePolicy(sizePolicy)
        self.ChooseLanguage_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ChooseLanguage_comboBox.setObjectName("ChooseLanguage_comboBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.ChooseLanguage_comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RenameTool"))
        self.label.setText(_translate("MainWindow", "字幕语言"))
        self.StartProcess.setText(_translate("MainWindow", "开始处理"))
        self.label_5.setText(_translate("MainWindow", "文件名匹配"))
        self.label_3.setText(_translate("MainWindow", "视频文件夹"))
        self.ChooseVIdeoPath_pushButton.setText(_translate("MainWindow", "浏览..."))
        self.label_2.setText(_translate("MainWindow", "字幕文件夹"))
        self.ChooseSubtitlePath_pushButton.setText(_translate("MainWindow", "浏览..."))
        self.label_4.setText(_translate("MainWindow", "新的文件名"))
