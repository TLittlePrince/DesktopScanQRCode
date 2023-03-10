# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jumpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 118)
        Form.setStyleSheet("")
        Form.setWindowOpacity(1)  # 设置窗口透明度
        Form.setWindowFlags(QtCore.Qt.WindowDoesNotAcceptFocus |
                            QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setStyleSheet("border: 1px solid rgb(152, 152, 152);\n"
                                      "border-radius: 16px;\n"
                                      "background-color: rgb(255, 255, 255);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        self.content_label.setFont(font)
        self.content_label.setStyleSheet("border-radius: 0;\n"
                                         "border: none;")
        self.content_label.setAlignment(QtCore.Qt.AlignCenter)
        self.content_label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.content_label.setObjectName("content_label")
        self.verticalLayout_2.addWidget(self.content_label)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setStyleSheet("border-radius: 0;\n"
                                    "border: none;")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(-1, 1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.copy_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_button.sizePolicy().hasHeightForWidth())
        self.copy_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.copy_button.setFont(font)
        self.copy_button.setObjectName("copy_button")
        self.horizontalLayout.addWidget(self.copy_button)
        self.jump_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jump_button.sizePolicy().hasHeightForWidth())
        self.jump_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.jump_button.setFont(font)
        self.jump_button.setObjectName("jump_button")
        self.horizontalLayout.addWidget(self.jump_button)
        self.close_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.close_button.setFont(font)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.show_window = QtWidgets.QAction(Form)
        self.show_window.setObjectName("show_window")
        self.quit = QtWidgets.QAction(Form)
        self.quit.setObjectName("quit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.content_label.setText(_translate("Form", "TextLabel"))
        self.copy_button.setText(_translate("Form", "复制"))
        self.jump_button.setText(_translate("Form", "跳转"))
        self.close_button.setText(_translate("Form", "关闭"))
        self.show_window.setText(_translate("Form", "恢复(&R)"))
        self.show_window.setToolTip(_translate("Form", "恢复显示窗口"))
        self.show_window.setShortcut(_translate("Form", "R"))
        self.quit.setText(_translate("Form", "退出(&Q)"))
