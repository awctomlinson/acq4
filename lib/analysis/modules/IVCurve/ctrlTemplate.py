# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/analysis/modules/IVCurve/ctrlTemplate.ui'
#
# Created: Tue Jan 15 15:29:34 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(326, 334)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setMargin(5)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.IVCurve_tau2TStart = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_tau2TStart.setFont(font)
        self.IVCurve_tau2TStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_tau2TStart.setDecimals(1)
        self.IVCurve_tau2TStart.setMaximum(5000.0)
        self.IVCurve_tau2TStart.setObjectName(_fromUtf8("IVCurve_tau2TStart"))
        self.gridLayout_3.addWidget(self.IVCurve_tau2TStart, 7, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 14, 0, 1, 1)
        self.IVCurve_ssTStop = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_ssTStop.setFont(font)
        self.IVCurve_ssTStop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_ssTStop.setMinimum(-5000.0)
        self.IVCurve_ssTStop.setMaximum(50000.0)
        self.IVCurve_ssTStop.setObjectName(_fromUtf8("IVCurve_ssTStop"))
        self.gridLayout_3.addWidget(self.IVCurve_ssTStop, 3, 1, 1, 2)
        self.IVCurve_tau2TStop = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_tau2TStop.setFont(font)
        self.IVCurve_tau2TStop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_tau2TStop.setMaximum(5000.0)
        self.IVCurve_tau2TStop.setObjectName(_fromUtf8("IVCurve_tau2TStop"))
        self.gridLayout_3.addWidget(self.IVCurve_tau2TStop, 7, 4, 1, 2)
        self.IVCurve_pkTStop = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_pkTStop.setFont(font)
        self.IVCurve_pkTStop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_pkTStop.setMinimum(-5000.0)
        self.IVCurve_pkTStop.setMaximum(50000.0)
        self.IVCurve_pkTStop.setObjectName(_fromUtf8("IVCurve_pkTStop"))
        self.gridLayout_3.addWidget(self.IVCurve_pkTStop, 5, 4, 1, 2)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 16, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 17, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 12, 0, 1, 1)
        self.IVCurve_Rin = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_Rin.setFont(font)
        self.IVCurve_Rin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_Rin.setReadOnly(True)
        self.IVCurve_Rin.setObjectName(_fromUtf8("IVCurve_Rin"))
        self.gridLayout_3.addWidget(self.IVCurve_Rin, 14, 2, 1, 1)
        self.IVCurve_pkTStart = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_pkTStart.setFont(font)
        self.IVCurve_pkTStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_pkTStart.setMinimum(-5000.0)
        self.IVCurve_pkTStart.setMaximum(50000.0)
        self.IVCurve_pkTStart.setObjectName(_fromUtf8("IVCurve_pkTStart"))
        self.gridLayout_3.addWidget(self.IVCurve_pkTStart, 5, 1, 1, 2)
        self.IVCurve_ssTStart = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_ssTStart.setFont(font)
        self.IVCurve_ssTStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_ssTStart.setMinimum(-5000.0)
        self.IVCurve_ssTStart.setMaximum(50000.0)
        self.IVCurve_ssTStart.setObjectName(_fromUtf8("IVCurve_ssTStart"))
        self.gridLayout_3.addWidget(self.IVCurve_ssTStart, 3, 4, 1, 2)
        self.IVCurve_AR = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_AR.setFont(font)
        self.IVCurve_AR.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_AR.setReadOnly(True)
        self.IVCurve_AR.setObjectName(_fromUtf8("IVCurve_AR"))
        self.gridLayout_3.addWidget(self.IVCurve_AR, 17, 2, 1, 1)
        self.IVCurve_Tau = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_Tau.setFont(font)
        self.IVCurve_Tau.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_Tau.setReadOnly(True)
        self.IVCurve_Tau.setObjectName(_fromUtf8("IVCurve_Tau"))
        self.gridLayout_3.addWidget(self.IVCurve_Tau, 16, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 8, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 18, 0, 1, 1)
        self.IVCurve_pkAmp = QtGui.QLineEdit(self.groupBox)
        self.IVCurve_pkAmp.setReadOnly(True)
        self.IVCurve_pkAmp.setObjectName(_fromUtf8("IVCurve_pkAmp"))
        self.gridLayout_3.addWidget(self.IVCurve_pkAmp, 18, 2, 1, 1)
        self.IVCurve_tauh_Commands = QtGui.QComboBox(self.groupBox)
        self.IVCurve_tauh_Commands.setObjectName(_fromUtf8("IVCurve_tauh_Commands"))
        self.IVCurve_tauh_Commands.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.IVCurve_tauh_Commands, 8, 4, 1, 2)
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 8, 3, 1, 1)
        self.IVCurve_showHide_lrss = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.IVCurve_showHide_lrss.setFont(font)
        self.IVCurve_showHide_lrss.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.IVCurve_showHide_lrss.setChecked(True)
        self.IVCurve_showHide_lrss.setObjectName(_fromUtf8("IVCurve_showHide_lrss"))
        self.gridLayout_3.addWidget(self.IVCurve_showHide_lrss, 3, 0, 1, 1)
        self.IVCurve_showHide_lrpk = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.IVCurve_showHide_lrpk.setFont(font)
        self.IVCurve_showHide_lrpk.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.IVCurve_showHide_lrpk.setChecked(True)
        self.IVCurve_showHide_lrpk.setObjectName(_fromUtf8("IVCurve_showHide_lrpk"))
        self.gridLayout_3.addWidget(self.IVCurve_showHide_lrpk, 5, 0, 1, 1)
        self.IVCurve_showHide_lrtau = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.IVCurve_showHide_lrtau.setFont(font)
        self.IVCurve_showHide_lrtau.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.IVCurve_showHide_lrtau.setAutoFillBackground(False)
        self.IVCurve_showHide_lrtau.setObjectName(_fromUtf8("IVCurve_showHide_lrtau"))
        self.gridLayout_3.addWidget(self.IVCurve_showHide_lrtau, 7, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 5, 1, 1)
        self.IVCurve_dataMode = QtGui.QLabel(self.groupBox)
        self.IVCurve_dataMode.setObjectName(_fromUtf8("IVCurve_dataMode"))
        self.gridLayout_3.addWidget(self.IVCurve_dataMode, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 13, 0, 1, 1)
        self.IVCurve_vrmp = QtGui.QLineEdit(self.groupBox)
        self.IVCurve_vrmp.setReadOnly(True)
        self.IVCurve_vrmp.setObjectName(_fromUtf8("IVCurve_vrmp"))
        self.gridLayout_3.addWidget(self.IVCurve_vrmp, 13, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 2, 1, 1)
        self.line = QtGui.QFrame(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 10, 0, 1, 6)
        self.IVCurve_PrintResults = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IVCurve_PrintResults.sizePolicy().hasHeightForWidth())
        self.IVCurve_PrintResults.setSizePolicy(sizePolicy)
        self.IVCurve_PrintResults.setObjectName(_fromUtf8("IVCurve_PrintResults"))
        self.gridLayout_3.addWidget(self.IVCurve_PrintResults, 12, 5, 1, 1)
        self.IVCurve_Update = QtGui.QPushButton(self.groupBox)
        self.IVCurve_Update.setObjectName(_fromUtf8("IVCurve_Update"))
        self.gridLayout_3.addWidget(self.IVCurve_Update, 12, 2, 1, 1)
        self.IVCurve_SpikeThreshold = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_SpikeThreshold.setFont(font)
        self.IVCurve_SpikeThreshold.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_SpikeThreshold.setDecimals(1)
        self.IVCurve_SpikeThreshold.setMinimum(-100.0)
        self.IVCurve_SpikeThreshold.setObjectName(_fromUtf8("IVCurve_SpikeThreshold"))
        self.gridLayout_3.addWidget(self.IVCurve_SpikeThreshold, 8, 1, 1, 2)
        self.dbStoreBtn = QtGui.QPushButton(self.groupBox)
        self.dbStoreBtn.setObjectName(_fromUtf8("dbStoreBtn"))
        self.gridLayout_3.addWidget(self.dbStoreBtn, 19, 3, 1, 3)
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 13, 3, 1, 1)
        self.IVCurve_Tauh = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_Tauh.setFont(font)
        self.IVCurve_Tauh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_Tauh.setReadOnly(True)
        self.IVCurve_Tauh.setObjectName(_fromUtf8("IVCurve_Tauh"))
        self.gridLayout_3.addWidget(self.IVCurve_Tauh, 13, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 14, 3, 1, 1)
        self.IVCurve_Ih_ba = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_Ih_ba.setFont(font)
        self.IVCurve_Ih_ba.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IVCurve_Ih_ba.setReadOnly(True)
        self.IVCurve_Ih_ba.setObjectName(_fromUtf8("IVCurve_Ih_ba"))
        self.gridLayout_3.addWidget(self.IVCurve_Ih_ba, 14, 5, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 16, 3, 1, 1)
        self.IVCurve_FOType = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IVCurve_FOType.setFont(font)
        self.IVCurve_FOType.setReadOnly(True)
        self.IVCurve_FOType.setObjectName(_fromUtf8("IVCurve_FOType"))
        self.gridLayout_3.addWidget(self.IVCurve_FOType, 16, 5, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 17, 3, 1, 1)
        self.IVCurve_ssAmp = QtGui.QLineEdit(self.groupBox)
        self.IVCurve_ssAmp.setReadOnly(True)
        self.IVCurve_ssAmp.setObjectName(_fromUtf8("IVCurve_ssAmp"))
        self.gridLayout_3.addWidget(self.IVCurve_ssAmp, 17, 5, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 18, 3, 1, 1)
        self.IVCurve_Gh = QtGui.QLineEdit(self.groupBox)
        self.IVCurve_Gh.setReadOnly(True)
        self.IVCurve_Gh.setObjectName(_fromUtf8("IVCurve_Gh"))
        self.gridLayout_3.addWidget(self.IVCurve_Gh, 18, 5, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "IV Analysis-V1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "R<sub>in</sub>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "&tau;<sub>m</sub> (ms)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Adapt \n"
"Ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Spike Thr", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Form", "Pk Amp", None, QtGui.QApplication.UnicodeUTF8))
        self.IVCurve_tauh_Commands.setItemText(0, QtGui.QApplication.translate("Form", "-0.6", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Form", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.IVCurve_showHide_lrss.setText(QtGui.QApplication.translate("Form", "IV:SS", None, QtGui.QApplication.UnicodeUTF8))
        self.IVCurve_showHide_lrpk.setText(QtGui.QApplication.translate("Form", "IV:Peak", None, QtGui.QApplication.UnicodeUTF8))
        self.IVCurve_showHide_lrtau.setText(QtGui.QApplication.translate("Form", "Ih tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "T Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.IVCurve_dataMode.setText(QtGui.QApplication.translate("Form", "IVCurve_dataMode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "RMP/I<sub>0</sub>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "T Start", None, QtGui.QApplication.UnicodeUTF8))
        self.IVCurve_PrintResults.setText(QtGui.QApplication.translate("Form", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.IVCurve_Update.setText(QtGui.QApplication.translate("Form", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.IVCurve_SpikeThreshold.setSuffix(QtGui.QApplication.translate("Form", " mV", None, QtGui.QApplication.UnicodeUTF8))
        self.dbStoreBtn.setText(QtGui.QApplication.translate("Form", "DB Store", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&tau;<span style=\" vertical-align:sub;\">h</span> (ms)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "b/a (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "F&O Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "SS Amp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Gh", None, QtGui.QApplication.UnicodeUTF8))
