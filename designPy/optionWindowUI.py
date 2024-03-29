# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designUi\optionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_optionWindow(object):
    def setupUi(self, optionWindow):
        optionWindow.setObjectName("optionWindow")
        optionWindow.resize(1033, 709)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 243, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 243, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 243, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 243, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        optionWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        optionWindow.setFont(font)
        optionWindow.setAnimated(True)
        optionWindow.setDocumentMode(False)
        optionWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(optionWindow)
        self.centralwidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayoutH = QtWidgets.QHBoxLayout()
        self.mainLayoutH.setObjectName("mainLayoutH")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainLayoutH.addItem(spacerItem)
        self.centerLayoutV = QtWidgets.QVBoxLayout()
        self.centerLayoutV.setObjectName("centerLayoutV")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.centerLayoutV.addItem(spacerItem1)
        self.titleLayoutH = QtWidgets.QHBoxLayout()
        self.titleLayoutH.setObjectName("titleLayoutH")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titleLayoutH.addItem(spacerItem2)
        self.titleLblL = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(62, 91, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 91, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.titleLblL.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLblL.setFont(font)
        self.titleLblL.setTextFormat(QtCore.Qt.RichText)
        self.titleLblL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleLblL.setWordWrap(False)
        self.titleLblL.setObjectName("titleLblL")
        self.titleLayoutH.addWidget(self.titleLblL)
        self.titleLblR = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(62, 91, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 91, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.titleLblR.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.titleLblR.setFont(font)
        self.titleLblR.setObjectName("titleLblR")
        self.titleLayoutH.addWidget(self.titleLblR)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titleLayoutH.addItem(spacerItem3)
        self.centerLayoutV.addLayout(self.titleLayoutH)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.centerLayoutV.addItem(spacerItem4)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"    left: 2px\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(100, 40))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.newDraftTab = QtWidgets.QWidget()
        self.newDraftTab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newDraftTab.setObjectName("newDraftTab")
        self.ndCentralLayout = QtWidgets.QVBoxLayout(self.newDraftTab)
        self.ndCentralLayout.setObjectName("ndCentralLayout")
        self.ndMainLayoutV = QtWidgets.QVBoxLayout()
        self.ndMainLayoutV.setSpacing(0)
        self.ndMainLayoutV.setObjectName("ndMainLayoutV")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem5)
        self.ndLbl1 = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndLbl1.setFont(font)
        self.ndLbl1.setAlignment(QtCore.Qt.AlignCenter)
        self.ndLbl1.setObjectName("ndLbl1")
        self.ndMainLayoutV.addWidget(self.ndLbl1)
        self.ndLbl2 = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndLbl2.setFont(font)
        self.ndLbl2.setAlignment(QtCore.Qt.AlignCenter)
        self.ndLbl2.setObjectName("ndLbl2")
        self.ndMainLayoutV.addWidget(self.ndLbl2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem6)
        self.ndBlockInputLayoutHO = QtWidgets.QHBoxLayout()
        self.ndBlockInputLayoutHO.setObjectName("ndBlockInputLayoutHO")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutHO.addItem(spacerItem7)
        self.ndBlockInputLayoutVO = QtWidgets.QVBoxLayout()
        self.ndBlockInputLayoutVO.setSpacing(7)
        self.ndBlockInputLayoutVO.setObjectName("ndBlockInputLayoutVO")
        self.ndBlockInputLayoutHI = QtWidgets.QHBoxLayout()
        self.ndBlockInputLayoutHI.setObjectName("ndBlockInputLayoutHI")
        self.ndBlockInputLayoutVIL = QtWidgets.QVBoxLayout()
        self.ndBlockInputLayoutVIL.setObjectName("ndBlockInputLayoutVIL")
        self.ndBlockInputLbl = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndBlockInputLbl.setFont(font)
        self.ndBlockInputLbl.setObjectName("ndBlockInputLbl")
        self.ndBlockInputLayoutVIL.addWidget(self.ndBlockInputLbl)
        self.ndSessionInputLbl = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndSessionInputLbl.setFont(font)
        self.ndSessionInputLbl.setObjectName("ndSessionInputLbl")
        self.ndBlockInputLayoutVIL.addWidget(self.ndSessionInputLbl)
        self.ndBlockInputLayoutHI.addLayout(self.ndBlockInputLayoutVIL)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutHI.addItem(spacerItem8)
        self.ndBlockInputLayoutVIR = QtWidgets.QVBoxLayout()
        self.ndBlockInputLayoutVIR.setObjectName("ndBlockInputLayoutVIR")
        self.ndBlockInput = QtWidgets.QLineEdit(self.newDraftTab)
        self.ndBlockInput.setFrame(True)
        self.ndBlockInput.setObjectName("ndBlockInput")
        self.ndBlockInputLayoutVIR.addWidget(self.ndBlockInput)
        self.ndSessionInput = QtWidgets.QLineEdit(self.newDraftTab)
        self.ndSessionInput.setFrame(True)
        self.ndSessionInput.setObjectName("ndSessionInput")
        self.ndBlockInputLayoutVIR.addWidget(self.ndSessionInput)
        self.ndBlockInputLayoutHI.addLayout(self.ndBlockInputLayoutVIR)
        self.ndBlockInputLayoutVO.addLayout(self.ndBlockInputLayoutHI)
        self.ndTotalBlockLine = QtWidgets.QFrame(self.newDraftTab)
        self.ndTotalBlockLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.ndTotalBlockLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ndTotalBlockLine.setObjectName("ndTotalBlockLine")
        self.ndBlockInputLayoutVO.addWidget(self.ndTotalBlockLine)
        self.ndTotalBlockLayoutH = QtWidgets.QHBoxLayout()
        self.ndTotalBlockLayoutH.setObjectName("ndTotalBlockLayoutH")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndTotalBlockLayoutH.addItem(spacerItem9)
        self.ndTotalBlockLbl = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndTotalBlockLbl.setFont(font)
        self.ndTotalBlockLbl.setObjectName("ndTotalBlockLbl")
        self.ndTotalBlockLayoutH.addWidget(self.ndTotalBlockLbl)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndTotalBlockLayoutH.addItem(spacerItem10)
        self.ndTotalBlockTxt = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndTotalBlockTxt.setFont(font)
        self.ndTotalBlockTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.ndTotalBlockTxt.setObjectName("ndTotalBlockTxt")
        self.ndTotalBlockLayoutH.addWidget(self.ndTotalBlockTxt)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndTotalBlockLayoutH.addItem(spacerItem11)
        self.ndTotalBlockLayoutH.setStretch(0, 6)
        self.ndTotalBlockLayoutH.setStretch(1, 4)
        self.ndTotalBlockLayoutH.setStretch(2, 1)
        self.ndTotalBlockLayoutH.setStretch(3, 3)
        self.ndTotalBlockLayoutH.setStretch(4, 6)
        self.ndBlockInputLayoutVO.addLayout(self.ndTotalBlockLayoutH)
        self.ndBlockInputLayoutHO.addLayout(self.ndBlockInputLayoutVO)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutHO.addItem(spacerItem12)
        self.ndBlockInputLayoutHO.setStretch(0, 5)
        self.ndBlockInputLayoutHO.setStretch(1, 6)
        self.ndBlockInputLayoutHO.setStretch(2, 5)
        self.ndMainLayoutV.addLayout(self.ndBlockInputLayoutHO)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem13)
        self.ndBlockInputLayoutH_3 = QtWidgets.QHBoxLayout()
        self.ndBlockInputLayoutH_3.setObjectName("ndBlockInputLayoutH_3")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutH_3.addItem(spacerItem14)
        self.ndRadioLayoutV = QtWidgets.QVBoxLayout()
        self.ndRadioLayoutV.setObjectName("ndRadioLayoutV")
        self.ndWordRadioBtn = QtWidgets.QRadioButton(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndWordRadioBtn.setFont(font)
        self.ndWordRadioBtn.setChecked(True)
        self.ndWordRadioBtn.setObjectName("ndWordRadioBtn")
        self.ndRadioLayoutV.addWidget(self.ndWordRadioBtn)
        self.ndMntRadioBtn = QtWidgets.QRadioButton(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndMntRadioBtn.setFont(font)
        self.ndMntRadioBtn.setChecked(False)
        self.ndMntRadioBtn.setObjectName("ndMntRadioBtn")
        self.ndRadioLayoutV.addWidget(self.ndMntRadioBtn)
        self.ndFreeRadioBtn = QtWidgets.QRadioButton(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndFreeRadioBtn.setFont(font)
        self.ndFreeRadioBtn.setChecked(False)
        self.ndFreeRadioBtn.setObjectName("ndFreeRadioBtn")
        self.ndRadioLayoutV.addWidget(self.ndFreeRadioBtn)
        self.ndBlockInputLayoutH_3.addLayout(self.ndRadioLayoutV)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutH_3.addItem(spacerItem15)
        self.ndBlockInputLayoutH_3.setStretch(0, 5)
        self.ndBlockInputLayoutH_3.setStretch(2, 5)
        self.ndMainLayoutV.addLayout(self.ndBlockInputLayoutH_3)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem16)
        self.ndBtnLayoutH = QtWidgets.QHBoxLayout()
        self.ndBtnLayoutH.setObjectName("ndBtnLayoutH")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBtnLayoutH.addItem(spacerItem17)
        self.ndQuitBtn = QtWidgets.QPushButton(self.newDraftTab)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.ndQuitBtn.setFont(font)
        self.ndQuitBtn.setObjectName("ndQuitBtn")
        self.ndBtnLayoutH.addWidget(self.ndQuitBtn)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBtnLayoutH.addItem(spacerItem18)
        self.ndStartBtn = QtWidgets.QPushButton(self.newDraftTab)
        self.ndStartBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.ndStartBtn.setFont(font)
        self.ndStartBtn.setObjectName("ndStartBtn")
        self.ndBtnLayoutH.addWidget(self.ndStartBtn)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBtnLayoutH.addItem(spacerItem19)
        self.ndBtnLayoutH.setStretch(0, 6)
        self.ndBtnLayoutH.setStretch(4, 6)
        self.ndMainLayoutV.addLayout(self.ndBtnLayoutH)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem20)
        self.ndMainLayoutV.setStretch(4, 10)
        self.ndMainLayoutV.setStretch(6, 7)
        self.ndMainLayoutV.setStretch(8, 7)
        self.ndCentralLayout.addLayout(self.ndMainLayoutV)
        self.tabWidget.addTab(self.newDraftTab, "")
        self.openDraftTab = QtWidgets.QWidget()
        self.openDraftTab.setObjectName("openDraftTab")
        self.odCentralLayout = QtWidgets.QHBoxLayout(self.openDraftTab)
        self.odCentralLayout.setObjectName("odCentralLayout")
        self.odMainLayoutH = QtWidgets.QVBoxLayout()
        self.odMainLayoutH.setSpacing(0)
        self.odMainLayoutH.setObjectName("odMainLayoutH")
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem21)
        self.odFileLayout = QtWidgets.QHBoxLayout()
        self.odFileLayout.setObjectName("odFileLayout")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odFileLayout.addItem(spacerItem22)
        self.odFilePathTxt = QtWidgets.QLineEdit(self.openDraftTab)
        self.odFilePathTxt.setReadOnly(True)
        self.odFilePathTxt.setObjectName("odFilePathTxt")
        self.odFileLayout.addWidget(self.odFilePathTxt)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odFileLayout.addItem(spacerItem23)
        self.odBrowseBtn = QtWidgets.QPushButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odBrowseBtn.setFont(font)
        self.odBrowseBtn.setObjectName("odBrowseBtn")
        self.odFileLayout.addWidget(self.odBrowseBtn)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odFileLayout.addItem(spacerItem24)
        self.odFileLayout.setStretch(0, 2)
        self.odFileLayout.setStretch(1, 10)
        self.odFileLayout.setStretch(2, 1)
        self.odFileLayout.setStretch(3, 3)
        self.odFileLayout.setStretch(4, 2)
        self.odMainLayoutH.addLayout(self.odFileLayout)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem25)
        self.odBlockInputLayoutH = QtWidgets.QHBoxLayout()
        self.odBlockInputLayoutH.setObjectName("odBlockInputLayoutH")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutH.addItem(spacerItem26)
        self.odBlockInputLayoutVO = QtWidgets.QVBoxLayout()
        self.odBlockInputLayoutVO.setSpacing(7)
        self.odBlockInputLayoutVO.setObjectName("odBlockInputLayoutVO")
        self.odBlockInputLayoutHI = QtWidgets.QHBoxLayout()
        self.odBlockInputLayoutHI.setObjectName("odBlockInputLayoutHI")
        self.odBlockInputLayoutVIL = QtWidgets.QVBoxLayout()
        self.odBlockInputLayoutVIL.setObjectName("odBlockInputLayoutVIL")
        self.odBlockInputLbl = QtWidgets.QLabel(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odBlockInputLbl.setFont(font)
        self.odBlockInputLbl.setObjectName("odBlockInputLbl")
        self.odBlockInputLayoutVIL.addWidget(self.odBlockInputLbl)
        self.odSessionInputLbl = QtWidgets.QLabel(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odSessionInputLbl.setFont(font)
        self.odSessionInputLbl.setObjectName("odSessionInputLbl")
        self.odBlockInputLayoutVIL.addWidget(self.odSessionInputLbl)
        self.odBlockInputLayoutHI.addLayout(self.odBlockInputLayoutVIL)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutHI.addItem(spacerItem27)
        self.odBlockInputLayoutVIR = QtWidgets.QVBoxLayout()
        self.odBlockInputLayoutVIR.setObjectName("odBlockInputLayoutVIR")
        self.odBlockInput = QtWidgets.QLineEdit(self.openDraftTab)
        self.odBlockInput.setFrame(True)
        self.odBlockInput.setObjectName("odBlockInput")
        self.odBlockInputLayoutVIR.addWidget(self.odBlockInput)
        self.odSessionInput = QtWidgets.QLineEdit(self.openDraftTab)
        self.odSessionInput.setFrame(True)
        self.odSessionInput.setObjectName("odSessionInput")
        self.odBlockInputLayoutVIR.addWidget(self.odSessionInput)
        self.odBlockInputLayoutHI.addLayout(self.odBlockInputLayoutVIR)
        self.odBlockInputLayoutVO.addLayout(self.odBlockInputLayoutHI)
        self.odTotalBlockLine = QtWidgets.QFrame(self.openDraftTab)
        self.odTotalBlockLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.odTotalBlockLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.odTotalBlockLine.setObjectName("odTotalBlockLine")
        self.odBlockInputLayoutVO.addWidget(self.odTotalBlockLine)
        self.odTotalBlockLayoutH = QtWidgets.QHBoxLayout()
        self.odTotalBlockLayoutH.setObjectName("odTotalBlockLayoutH")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odTotalBlockLayoutH.addItem(spacerItem28)
        self.odTotalBlockLbl = QtWidgets.QLabel(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odTotalBlockLbl.setFont(font)
        self.odTotalBlockLbl.setObjectName("odTotalBlockLbl")
        self.odTotalBlockLayoutH.addWidget(self.odTotalBlockLbl)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odTotalBlockLayoutH.addItem(spacerItem29)
        self.odTotalBlockTxt = QtWidgets.QLabel(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odTotalBlockTxt.setFont(font)
        self.odTotalBlockTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.odTotalBlockTxt.setObjectName("odTotalBlockTxt")
        self.odTotalBlockLayoutH.addWidget(self.odTotalBlockTxt)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odTotalBlockLayoutH.addItem(spacerItem30)
        self.odTotalBlockLayoutH.setStretch(0, 6)
        self.odTotalBlockLayoutH.setStretch(1, 4)
        self.odTotalBlockLayoutH.setStretch(2, 1)
        self.odTotalBlockLayoutH.setStretch(3, 3)
        self.odTotalBlockLayoutH.setStretch(4, 6)
        self.odBlockInputLayoutVO.addLayout(self.odTotalBlockLayoutH)
        self.odBlockInputLayoutH.addLayout(self.odBlockInputLayoutVO)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutH.addItem(spacerItem31)
        self.odBlockInputLayoutH.setStretch(0, 5)
        self.odBlockInputLayoutH.setStretch(1, 6)
        self.odBlockInputLayoutH.setStretch(2, 5)
        self.odMainLayoutH.addLayout(self.odBlockInputLayoutH)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem32)
        self.odBlockInputLayoutH_2 = QtWidgets.QHBoxLayout()
        self.odBlockInputLayoutH_2.setObjectName("odBlockInputLayoutH_2")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutH_2.addItem(spacerItem33)
        self.odRadioLayoutV = QtWidgets.QVBoxLayout()
        self.odRadioLayoutV.setObjectName("odRadioLayoutV")
        self.odWordRadioBtn = QtWidgets.QRadioButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odWordRadioBtn.setFont(font)
        self.odWordRadioBtn.setChecked(True)
        self.odWordRadioBtn.setObjectName("odWordRadioBtn")
        self.odRadioLayoutV.addWidget(self.odWordRadioBtn)
        self.odMntRadioBtn = QtWidgets.QRadioButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odMntRadioBtn.setFont(font)
        self.odMntRadioBtn.setChecked(False)
        self.odMntRadioBtn.setObjectName("odMntRadioBtn")
        self.odRadioLayoutV.addWidget(self.odMntRadioBtn)
        self.odFreeRadioBtn = QtWidgets.QRadioButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odFreeRadioBtn.setFont(font)
        self.odFreeRadioBtn.setChecked(False)
        self.odFreeRadioBtn.setObjectName("odFreeRadioBtn")
        self.odRadioLayoutV.addWidget(self.odFreeRadioBtn)
        self.odBlockInputLayoutH_2.addLayout(self.odRadioLayoutV)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutH_2.addItem(spacerItem34)
        self.odBlockInputLayoutH_2.setStretch(0, 5)
        self.odBlockInputLayoutH_2.setStretch(2, 5)
        self.odMainLayoutH.addLayout(self.odBlockInputLayoutH_2)
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem35)
        self.odBtnLayoutH = QtWidgets.QHBoxLayout()
        self.odBtnLayoutH.setObjectName("odBtnLayoutH")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBtnLayoutH.addItem(spacerItem36)
        self.odQuitBtn = QtWidgets.QPushButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.odQuitBtn.setFont(font)
        self.odQuitBtn.setObjectName("odQuitBtn")
        self.odBtnLayoutH.addWidget(self.odQuitBtn)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBtnLayoutH.addItem(spacerItem37)
        self.odStartBtn = QtWidgets.QPushButton(self.openDraftTab)
        self.odStartBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.odStartBtn.setFont(font)
        self.odStartBtn.setObjectName("odStartBtn")
        self.odBtnLayoutH.addWidget(self.odStartBtn)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBtnLayoutH.addItem(spacerItem38)
        self.odBtnLayoutH.setStretch(0, 6)
        self.odBtnLayoutH.setStretch(4, 6)
        self.odMainLayoutH.addLayout(self.odBtnLayoutH)
        spacerItem39 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem39)
        self.odMainLayoutH.setStretch(3, 7)
        self.odMainLayoutH.setStretch(5, 7)
        self.odMainLayoutH.setStretch(7, 7)
        self.odCentralLayout.addLayout(self.odMainLayoutH)
        self.tabWidget.addTab(self.openDraftTab, "")
        self.centerLayoutV.addWidget(self.tabWidget)
        spacerItem40 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.centerLayoutV.addItem(spacerItem40)
        self.centerLayoutV.setStretch(1, 1)
        self.centerLayoutV.setStretch(2, 5)
        self.centerLayoutV.setStretch(3, 9)
        self.centerLayoutV.setStretch(4, 9)
        self.mainLayoutH.addLayout(self.centerLayoutV)
        spacerItem41 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainLayoutH.addItem(spacerItem41)
        self.mainLayoutH.setStretch(0, 5)
        self.mainLayoutH.setStretch(1, 4)
        self.mainLayoutH.setStretch(2, 5)
        self.verticalLayout.addLayout(self.mainLayoutH)
        self.bottomBtnsHLayout = QtWidgets.QHBoxLayout()
        self.bottomBtnsHLayout.setObjectName("bottomBtnsHLayout")
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomBtnsHLayout.addItem(spacerItem42)
        self.settingsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.settingsBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\designUi\\../img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon)
        self.settingsBtn.setIconSize(QtCore.QSize(45, 45))
        self.settingsBtn.setFlat(True)
        self.settingsBtn.setObjectName("settingsBtn")
        self.bottomBtnsHLayout.addWidget(self.settingsBtn)
        self.verticalLayout.addLayout(self.bottomBtnsHLayout)
        optionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(optionWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(optionWindow)

    def retranslateUi(self, optionWindow):
        _translate = QtCore.QCoreApplication.translate
        optionWindow.setWindowTitle(_translate("optionWindow", "optionWindow"))
        self.titleLblL.setText(_translate("optionWindow", "KEYBOARD"))
        self.titleLblR.setText(_translate("optionWindow", "COWBOY"))
        self.ndLbl1.setText(_translate("optionWindow", "You\'ll be able to save your work when you finish."))
        self.ndLbl2.setText(_translate("optionWindow", "Periodic auto-saves are stored in your \"My Documents\" folder."))
        self.ndBlockInputLbl.setText(_translate("optionWindow", "Block everthing until:"))
        self.ndSessionInputLbl.setText(_translate("optionWindow", "Num of Sessions:"))
        self.ndSessionInput.setText(_translate("optionWindow", "1"))
        self.ndSessionInput.setPlaceholderText(_translate("optionWindow", "1"))
        self.ndTotalBlockLbl.setText(_translate("optionWindow", "Total Goal:"))
        self.ndTotalBlockTxt.setText(_translate("optionWindow", "0"))
        self.ndWordRadioBtn.setText(_translate("optionWindow", "Words are typed."))
        self.ndMntRadioBtn.setText(_translate("optionWindow", "Minutes from now."))
        self.ndFreeRadioBtn.setText(_translate("optionWindow", "Don\'t block me."))
        self.ndQuitBtn.setText(_translate("optionWindow", "Quit"))
        self.ndStartBtn.setText(_translate("optionWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newDraftTab), _translate("optionWindow", "                 New Draft                  "))
        self.odBrowseBtn.setText(_translate("optionWindow", "Browse..."))
        self.odBlockInputLbl.setText(_translate("optionWindow", "Block everthing until:"))
        self.odSessionInputLbl.setText(_translate("optionWindow", "Num of Sessions:"))
        self.odSessionInput.setText(_translate("optionWindow", "1"))
        self.odSessionInput.setPlaceholderText(_translate("optionWindow", "1"))
        self.odTotalBlockLbl.setText(_translate("optionWindow", "Total Goal:"))
        self.odTotalBlockTxt.setText(_translate("optionWindow", "0"))
        self.odWordRadioBtn.setText(_translate("optionWindow", "Words are typed."))
        self.odMntRadioBtn.setText(_translate("optionWindow", "Minutes from now."))
        self.odFreeRadioBtn.setText(_translate("optionWindow", "Don\'t block me."))
        self.odQuitBtn.setText(_translate("optionWindow", "Quit"))
        self.odStartBtn.setText(_translate("optionWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.openDraftTab), _translate("optionWindow", "                 Open Draft                  "))
