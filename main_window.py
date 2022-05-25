# Form implementation generated from reading ui file 'qtui\mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutControl = QtWidgets.QVBoxLayout()
        self.verticalLayoutControl.setObjectName("verticalLayoutControl")
        self.labelControlSystem = QtWidgets.QLabel(self.centralWidget)
        self.labelControlSystem.setObjectName("labelControlSystem")
        self.verticalLayoutControl.addWidget(self.labelControlSystem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonConnectServer = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonConnectServer.setObjectName("pushButtonConnectServer")
        self.horizontalLayout.addWidget(self.pushButtonConnectServer)
        self.verticalLayoutControl.addLayout(self.horizontalLayout)
        self.horizontalLayoutControl = QtWidgets.QHBoxLayout()
        self.horizontalLayoutControl.setObjectName("horizontalLayoutControl")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelLoop = QtWidgets.QLabel(self.centralWidget)
        self.labelLoop.setObjectName("labelLoop")
        self.verticalLayout_2.addWidget(self.labelLoop)
        self.comboBoxLoop = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxLoop.setObjectName("comboBoxLoop")
        self.comboBoxLoop.addItem("")
        self.comboBoxLoop.addItem("")
        self.verticalLayout_2.addWidget(self.comboBoxLoop)
        self.horizontalLayoutControl.addLayout(self.verticalLayout_2)
        self.verticalLayoutControl.addLayout(self.horizontalLayoutControl)
        self.verticalLayout_3.addLayout(self.verticalLayoutControl)
        self.horizontalLine_1 = QtWidgets.QFrame(self.centralWidget)
        self.horizontalLine_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.horizontalLine_1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.horizontalLine_1.setObjectName("horizontalLine_1")
        self.verticalLayout_3.addWidget(self.horizontalLine_1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.inputWaveFormLabel = QtWidgets.QLabel(self.centralWidget)
        self.inputWaveFormLabel.setObjectName("inputWaveFormLabel")
        self.verticalLayout_7.addWidget(self.inputWaveFormLabel)
        self.comboBoxWaveForm = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxWaveForm.setObjectName("comboBoxWaveForm")
        self.comboBoxWaveForm.addItem("")
        self.comboBoxWaveForm.addItem("")
        self.comboBoxWaveForm.addItem("")
        self.comboBoxWaveForm.addItem("")
        self.comboBoxWaveForm.addItem("")
        self.verticalLayout_7.addWidget(self.comboBoxWaveForm)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.referenceWaveFormLabel = QtWidgets.QLabel(self.centralWidget)
        self.referenceWaveFormLabel.setObjectName("referenceWaveFormLabel")
        self.verticalLayout_8.addWidget(self.referenceWaveFormLabel)
        self.comboBoxReferenceWaveForm = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxReferenceWaveForm.setObjectName("comboBoxReferenceWaveForm")
        self.comboBoxReferenceWaveForm.addItem("")
        self.comboBoxReferenceWaveForm.addItem("")
        self.comboBoxReferenceWaveForm.addItem("")
        self.comboBoxReferenceWaveForm.addItem("")
        self.comboBoxReferenceWaveForm.addItem("")
        self.verticalLayout_8.addWidget(self.comboBoxReferenceWaveForm)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        self.horizontalLine_2 = QtWidgets.QFrame(self.centralWidget)
        self.horizontalLine_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.horizontalLine_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.horizontalLine_2.setObjectName("horizontalLine_2")
        self.verticalLayout_3.addWidget(self.horizontalLine_2)
        self.verticalLayoutParameters = QtWidgets.QVBoxLayout()
        self.verticalLayoutParameters.setObjectName("verticalLayoutParameters")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.labelMaxAmplitude = QtWidgets.QLabel(self.centralWidget)
        self.labelMaxAmplitude.setObjectName("labelMaxAmplitude")
        self.horizontalLayout_11.addWidget(self.labelMaxAmplitude)
        self.doubleBoxMaxAmplitude = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxMaxAmplitude.setMinimum(0.0)
        self.doubleBoxMaxAmplitude.setMaximum(9999.0)
        self.doubleBoxMaxAmplitude.setSingleStep(0.1)
        self.doubleBoxMaxAmplitude.setProperty("value", 10.0)
        self.doubleBoxMaxAmplitude.setObjectName("doubleBoxMaxAmplitude")
        self.horizontalLayout_11.addWidget(self.doubleBoxMaxAmplitude)
        self.verticalLayoutParameters.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelMinAmplitude = QtWidgets.QLabel(self.centralWidget)
        self.labelMinAmplitude.setObjectName("labelMinAmplitude")
        self.horizontalLayout_12.addWidget(self.labelMinAmplitude)
        self.doubleBoxMinAmplitude = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxMinAmplitude.setEnabled(False)
        self.doubleBoxMinAmplitude.setMinimum(-9999.0)
        self.doubleBoxMinAmplitude.setMaximum(0.0)
        self.doubleBoxMinAmplitude.setSingleStep(0.1)
        self.doubleBoxMinAmplitude.setObjectName("doubleBoxMinAmplitude")
        self.horizontalLayout_12.addWidget(self.doubleBoxMinAmplitude)
        self.verticalLayoutParameters.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelMaxPeriod = QtWidgets.QLabel(self.centralWidget)
        self.labelMaxPeriod.setObjectName("labelMaxPeriod")
        self.horizontalLayout_13.addWidget(self.labelMaxPeriod)
        self.doubleBoxMaxPeriod = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxMaxPeriod.setMinimum(0.01)
        self.doubleBoxMaxPeriod.setMaximum(9999.0)
        self.doubleBoxMaxPeriod.setSingleStep(0.1)
        self.doubleBoxMaxPeriod.setProperty("value", 6.28)
        self.doubleBoxMaxPeriod.setObjectName("doubleBoxMaxPeriod")
        self.horizontalLayout_13.addWidget(self.doubleBoxMaxPeriod)
        self.verticalLayoutParameters.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelMinPeriod = QtWidgets.QLabel(self.centralWidget)
        self.labelMinPeriod.setObjectName("labelMinPeriod")
        self.horizontalLayout_10.addWidget(self.labelMinPeriod)
        self.doubleBoxMinPeriod = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxMinPeriod.setEnabled(False)
        self.doubleBoxMinPeriod.setMinimum(0.01)
        self.doubleBoxMinPeriod.setMaximum(9999.0)
        self.doubleBoxMinPeriod.setSingleStep(0.1)
        self.doubleBoxMinPeriod.setProperty("value", 0.1)
        self.doubleBoxMinPeriod.setObjectName("doubleBoxMinPeriod")
        self.horizontalLayout_10.addWidget(self.doubleBoxMinPeriod)
        self.verticalLayoutParameters.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.labelOffset = QtWidgets.QLabel(self.centralWidget)
        self.labelOffset.setObjectName("labelOffset")
        self.horizontalLayout_14.addWidget(self.labelOffset)
        self.doubleBoxOffset = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxOffset.setMinimum(-9999.0)
        self.doubleBoxOffset.setMaximum(9999.0)
        self.doubleBoxOffset.setSingleStep(0.01)
        self.doubleBoxOffset.setObjectName("doubleBoxOffset")
        self.horizontalLayout_14.addWidget(self.doubleBoxOffset)
        self.verticalLayoutParameters.addLayout(self.horizontalLayout_14)
        self.verticalLayout_3.addLayout(self.verticalLayoutParameters)
        self.horizontalLine_3 = QtWidgets.QFrame(self.centralWidget)
        self.horizontalLine_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.horizontalLine_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.horizontalLine_3.setObjectName("horizontalLine_3")
        self.verticalLayout_3.addWidget(self.horizontalLine_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.controllerFormLabel_2 = QtWidgets.QLabel(self.centralWidget)
        self.controllerFormLabel_2.setObjectName("controllerFormLabel_2")
        self.horizontalLayout_9.addWidget(self.controllerFormLabel_2)
        self.comboBoxOutput = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxOutput.setObjectName("comboBoxOutput")
        self.comboBoxOutput.addItem("")
        self.comboBoxOutput.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBoxOutput)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.controllerFormLabel = QtWidgets.QLabel(self.centralWidget)
        self.controllerFormLabel.setObjectName("controllerFormLabel")
        self.verticalLayout_10.addWidget(self.controllerFormLabel)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBoxController = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxController.setObjectName("comboBoxController")
        self.comboBoxController.addItem("")
        self.comboBoxController.addItem("")
        self.comboBoxController.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBoxController)
        self.pushButtonControl = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonControl.setObjectName("pushButtonControl")
        self.horizontalLayout_7.addWidget(self.pushButtonControl)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.controllerKpLabel = QtWidgets.QLabel(self.centralWidget)
        self.controllerKpLabel.setObjectName("controllerKpLabel")
        self.horizontalLayout_2.addWidget(self.controllerKpLabel)
        self.doubleBoxKp = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxKp.setMinimum(0.0)
        self.doubleBoxKp.setMaximum(50.0)
        self.doubleBoxKp.setSingleStep(0.1)
        self.doubleBoxKp.setProperty("value", 0.0)
        self.doubleBoxKp.setObjectName("doubleBoxKp")
        self.horizontalLayout_2.addWidget(self.doubleBoxKp)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.controllerKdLabel = QtWidgets.QLabel(self.centralWidget)
        self.controllerKdLabel.setObjectName("controllerKdLabel")
        self.horizontalLayout_3.addWidget(self.controllerKdLabel)
        self.doubleBoxKd = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxKd.setMinimum(0.0)
        self.doubleBoxKd.setMaximum(50.0)
        self.doubleBoxKd.setSingleStep(0.1)
        self.doubleBoxKd.setProperty("value", 0.0)
        self.doubleBoxKd.setObjectName("doubleBoxKd")
        self.horizontalLayout_3.addWidget(self.doubleBoxKd)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.controllerKiLabel = QtWidgets.QLabel(self.centralWidget)
        self.controllerKiLabel.setObjectName("controllerKiLabel")
        self.horizontalLayout_4.addWidget(self.controllerKiLabel)
        self.doubleBoxKi = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxKi.setMinimum(0.0)
        self.doubleBoxKi.setMaximum(50.0)
        self.doubleBoxKi.setSingleStep(0.1)
        self.doubleBoxKi.setProperty("value", 0.0)
        self.doubleBoxKi.setObjectName("doubleBoxKi")
        self.horizontalLayout_4.addWidget(self.doubleBoxKi)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.controllerTdLabel = QtWidgets.QLabel(self.centralWidget)
        self.controllerTdLabel.setObjectName("controllerTdLabel")
        self.horizontalLayout_5.addWidget(self.controllerTdLabel)
        self.doubleBoxTd = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxTd.setMinimum(0.0)
        self.doubleBoxTd.setMaximum(50.0)
        self.doubleBoxTd.setSingleStep(0.1)
        self.doubleBoxTd.setProperty("value", 0.0)
        self.doubleBoxTd.setObjectName("doubleBoxTd")
        self.horizontalLayout_5.addWidget(self.doubleBoxTd)
        self.verticalLayout_12.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.controllerTdLabel_2 = QtWidgets.QLabel(self.centralWidget)
        self.controllerTdLabel_2.setObjectName("controllerTdLabel_2")
        self.horizontalLayout_6.addWidget(self.controllerTdLabel_2)
        self.doubleBoxTi = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleBoxTi.setMinimum(0.0)
        self.doubleBoxTi.setMaximum(50.0)
        self.doubleBoxTi.setSingleStep(0.1)
        self.doubleBoxTi.setProperty("value", 0.0)
        self.doubleBoxTi.setObjectName("doubleBoxTi")
        self.horizontalLayout_6.addWidget(self.doubleBoxTi)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_23.addLayout(self.verticalLayout_3)
        self.verticalLine = QtWidgets.QFrame(self.centralWidget)
        self.verticalLine.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.verticalLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.verticalLine.setObjectName("verticalLine")
        self.horizontalLayout_23.addWidget(self.verticalLine)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.labelIAE = QtWidgets.QLabel(self.centralWidget)
        self.labelIAE.setObjectName("labelIAE")
        self.horizontalLayout_15.addWidget(self.labelIAE)
        self.lcdNumberIAE = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumberIAE.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.lcdNumberIAE.setSmallDecimalPoint(False)
        self.lcdNumberIAE.setDigitCount(10)
        self.lcdNumberIAE.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumberIAE.setObjectName("lcdNumberIAE")
        self.horizontalLayout_15.addWidget(self.lcdNumberIAE)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.labelISE = QtWidgets.QLabel(self.centralWidget)
        self.labelISE.setObjectName("labelISE")
        self.horizontalLayout_17.addWidget(self.labelISE)
        self.lcdNumberISE = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumberISE.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.lcdNumberISE.setDigitCount(10)
        self.lcdNumberISE.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumberISE.setObjectName("lcdNumberISE")
        self.horizontalLayout_17.addWidget(self.lcdNumberISE)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_17)
        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.labeITAE = QtWidgets.QLabel(self.centralWidget)
        self.labeITAE.setObjectName("labeITAE")
        self.horizontalLayout_18.addWidget(self.labeITAE)
        self.lcdNumberITAE = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumberITAE.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.lcdNumberITAE.setDigitCount(10)
        self.lcdNumberITAE.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumberITAE.setObjectName("lcdNumberITAE")
        self.horizontalLayout_18.addWidget(self.lcdNumberITAE)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.labeIGoodHeart = QtWidgets.QLabel(self.centralWidget)
        self.labeIGoodHeart.setObjectName("labeIGoodHeart")
        self.horizontalLayout_20.addWidget(self.labeIGoodHeart)
        self.lcdNumberGoodHeart = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumberGoodHeart.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.lcdNumberGoodHeart.setDigitCount(10)
        self.lcdNumberGoodHeart.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumberGoodHeart.setObjectName("lcdNumberGoodHeart")
        self.horizontalLayout_20.addWidget(self.lcdNumberGoodHeart)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.graphWidgetLayout = QtWidgets.QHBoxLayout()
        self.graphWidgetLayout.setContentsMargins(0, -1, -1, -1)
        self.graphWidgetLayout.setObjectName("graphWidgetLayout")
        self.verticalLayout_4.addLayout(self.graphWidgetLayout)
        self.horizontalLayout_23.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
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
        self.labelControlSystem.setText(_translate("MainWindow", "Control System"))
        self.pushButtonConnectServer.setText(_translate("MainWindow", "Connect to Server"))
        self.labelLoop.setText(_translate("MainWindow", "Loop"))
        self.comboBoxLoop.setItemText(0, _translate("MainWindow", "Open"))
        self.comboBoxLoop.setItemText(1, _translate("MainWindow", "Closed"))
        self.inputWaveFormLabel.setText(_translate("MainWindow", "Input Wave Form"))
        self.comboBoxWaveForm.setItemText(0, _translate("MainWindow", "step"))
        self.comboBoxWaveForm.setItemText(1, _translate("MainWindow", "sine"))
        self.comboBoxWaveForm.setItemText(2, _translate("MainWindow", "square"))
        self.comboBoxWaveForm.setItemText(3, _translate("MainWindow", "sawtooth"))
        self.comboBoxWaveForm.setItemText(4, _translate("MainWindow", "random"))
        self.referenceWaveFormLabel.setText(_translate("MainWindow", "Reference Wave Form"))
        self.comboBoxReferenceWaveForm.setItemText(0, _translate("MainWindow", "step"))
        self.comboBoxReferenceWaveForm.setItemText(1, _translate("MainWindow", "sine"))
        self.comboBoxReferenceWaveForm.setItemText(2, _translate("MainWindow", "square"))
        self.comboBoxReferenceWaveForm.setItemText(3, _translate("MainWindow", "sawtooth"))
        self.comboBoxReferenceWaveForm.setItemText(4, _translate("MainWindow", "random"))
        self.labelMaxAmplitude.setText(_translate("MainWindow", "Amplitude"))
        self.labelMinAmplitude.setText(_translate("MainWindow", "Min Amplitude"))
        self.labelMaxPeriod.setText(_translate("MainWindow", "Period"))
        self.labelMinPeriod.setText(_translate("MainWindow", "Min Period"))
        self.labelOffset.setText(_translate("MainWindow", "Offset"))
        self.controllerFormLabel_2.setText(_translate("MainWindow", "Output"))
        self.comboBoxOutput.setItemText(0, _translate("MainWindow", "Block I - Red"))
        self.comboBoxOutput.setItemText(1, _translate("MainWindow", "Block II - Green"))
        self.controllerFormLabel.setText(_translate("MainWindow", "Controller"))
        self.comboBoxController.setItemText(0, _translate("MainWindow", "PID"))
        self.comboBoxController.setItemText(1, _translate("MainWindow", "PI-D"))
        self.comboBoxController.setItemText(2, _translate("MainWindow", "I-PD"))
        self.pushButtonControl.setText(_translate("MainWindow", "Control"))
        self.controllerKpLabel.setText(_translate("MainWindow", "Kp"))
        self.controllerKdLabel.setText(_translate("MainWindow", "Kd"))
        self.controllerKiLabel.setText(_translate("MainWindow", "Ki"))
        self.controllerTdLabel.setText(_translate("MainWindow", "Td"))
        self.controllerTdLabel_2.setText(_translate("MainWindow", "Ti"))
        self.labelIAE.setText(_translate("MainWindow", "IAE"))
        self.labelISE.setText(_translate("MainWindow", "ISE"))
        self.labeITAE.setText(_translate("MainWindow", "ITAE"))
        self.labeIGoodHeart.setText(_translate("MainWindow", "Goodhart"))
