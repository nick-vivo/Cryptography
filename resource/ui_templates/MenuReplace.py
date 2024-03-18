# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'footerMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_footerMenu(object):
	def setupUi(self, footerMenu):
		footerMenu.setObjectName("footerMenu")
		footerMenu.resize(800, 807)
		font = QtGui.QFont()
		font.setFamily("C059")
		font.setPointSize(19)
		footerMenu.setFont(font)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../icons/label5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		footerMenu.setWindowIcon(icon)
		self.footerMenu_central = QtWidgets.QWidget(footerMenu)
		self.footerMenu_central.setObjectName("footerMenu_central")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.footerMenu_central)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.footerMenu_content = QtWidgets.QFrame(self.footerMenu_central)
		self.footerMenu_content.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.footerMenu_content.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.footerMenu_content.setFrameShadow(QtWidgets.QFrame.Plain)
		self.footerMenu_content.setLineWidth(0)
		self.footerMenu_content.setObjectName("footerMenu_content")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.footerMenu_content)
		self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.footer = QtWidgets.QFrame(self.footerMenu_content)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
		self.footer.setSizePolicy(sizePolicy)
		self.footer.setMaximumSize(QtCore.QSize(16777215, 50))
		self.footer.setStyleSheet("")
		self.footer.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
		self.footer.setLineWidth(0)
		self.footer.setObjectName("footer")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.footer)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.fName = QtWidgets.QFrame(self.footer)
		self.fName.setMinimumSize(QtCore.QSize(0, 0))
		self.fName.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.fName.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.fName.setFrameShadow(QtWidgets.QFrame.Raised)
		self.fName.setLineWidth(0)
		self.fName.setObjectName("fName")
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fName)
		self.horizontalLayout_7.setContentsMargins(0, 5, 0, 0)
		self.horizontalLayout_7.setSpacing(0)
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.fText = QtWidgets.QFrame(self.fName)
		self.fText.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.fText.setFrameShadow(QtWidgets.QFrame.Raised)
		self.fText.setLineWidth(0)
		self.fText.setObjectName("fText")
		self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.fText)
		self.horizontalLayout_9.setContentsMargins(20, 0, 0, 0)
		self.horizontalLayout_9.setSpacing(0)
		self.horizontalLayout_9.setObjectName("horizontalLayout_9")
		self.flText = QtWidgets.QLabel(self.fText)
		self.flText.setMaximumSize(QtCore.QSize(16777215, 16777215))
		font = QtGui.QFont()
		font.setFamily("C059")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.flText.setFont(font)
		self.flText.setScaledContents(True)
		self.flText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.flText.setObjectName("flText")
		self.horizontalLayout_9.addWidget(self.flText)
		self.horizontalLayout_7.addWidget(self.fText)
		self.horizontalLayout_7.setStretch(0, 70)
		self.horizontalLayout.addWidget(self.fName)
		self.fButtons = QtWidgets.QFrame(self.footer)
		self.fButtons.setMinimumSize(QtCore.QSize(0, 50))
		self.fButtons.setMaximumSize(QtCore.QSize(16777215, 50))
		self.fButtons.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.fButtons.setFrameShadow(QtWidgets.QFrame.Raised)
		self.fButtons.setLineWidth(0)
		self.fButtons.setObjectName("fButtons")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fButtons)
		self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_3.setSpacing(0)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.fBlock = QtWidgets.QFrame(self.fButtons)
		self.fBlock.setMinimumSize(QtCore.QSize(0, 0))
		self.fBlock.setMaximumSize(QtCore.QSize(16777215, 48))
		self.fBlock.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.fBlock.setFrameShadow(QtWidgets.QFrame.Raised)
		self.fBlock.setLineWidth(0)
		self.fBlock.setObjectName("fBlock")
		self.horizontalLayout_3.addWidget(self.fBlock)
		self.fbuttons = QtWidgets.QFrame(self.fButtons)
		self.fbuttons.setMinimumSize(QtCore.QSize(200, 0))
		self.fbuttons.setMaximumSize(QtCore.QSize(200, 48))
		self.fbuttons.setStyleSheet("QPushButton:hover\n"
"{\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(184, 186, 188, 0.4);\n"
"}")
		self.fbuttons.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.fbuttons.setFrameShadow(QtWidgets.QFrame.Raised)
		self.fbuttons.setLineWidth(0)
		self.fbuttons.setObjectName("fbuttons")
		self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.fbuttons)
		self.horizontalLayout_10.setContentsMargins(0, 0, 10, 1)
		self.horizontalLayout_10.setSpacing(20)
		self.horizontalLayout_10.setObjectName("horizontalLayout_10")
		self.collaps = QtWidgets.QPushButton(self.fbuttons)
		self.collaps.setMinimumSize(QtCore.QSize(0, 40))
		self.collaps.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.collaps.setStyleSheet("QPushButton:hover\n"
"{\n"
"	background: rgb(255, 190, 111);\n"
"}\n"
"")
		self.collaps.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("../icons/collaps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.collaps.setIcon(icon1)
		self.collaps.setIconSize(QtCore.QSize(30, 30))
		self.collaps.setCheckable(False)
		self.collaps.setObjectName("collaps")
		self.horizontalLayout_10.addWidget(self.collaps)
		self.more = QtWidgets.QPushButton(self.fbuttons)
		self.more.setMinimumSize(QtCore.QSize(0, 0))
		self.more.setStyleSheet("QPushButton:hover\n"
"{\n"
"	background: rgb(153, 193, 241);\n"
"}\n"
"")
		self.more.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("../icons/more_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.more.setIcon(icon2)
		self.more.setIconSize(QtCore.QSize(30, 40))
		self.more.setObjectName("more")
		self.horizontalLayout_10.addWidget(self.more)
		self.exit = QtWidgets.QPushButton(self.fbuttons)
		self.exit.setMinimumSize(QtCore.QSize(0, 0))
		self.exit.setStyleSheet("QPushButton:hover\n"
"{\n"
"	background: rgb(246, 97, 81);\n"
"}\n"
"")
		self.exit.setText("")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("../icons/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.exit.setIcon(icon3)
		self.exit.setIconSize(QtCore.QSize(40, 40))
		self.exit.setObjectName("exit")
		self.horizontalLayout_10.addWidget(self.exit)
		self.horizontalLayout_3.addWidget(self.fbuttons)
		self.horizontalLayout_3.setStretch(0, 60)
		self.horizontalLayout_3.setStretch(1, 40)
		self.horizontalLayout.addWidget(self.fButtons)
		self.horizontalLayout.setStretch(0, 50)
		self.horizontalLayout.setStretch(1, 50)
		self.verticalLayout_3.addWidget(self.footer)
		self.MenuBase = QtWidgets.QFrame(self.footerMenu_content)
		self.MenuBase.setStyleSheet("QPushButton:hover\n"
"{\n"
"	background-position: center;\n"
"	background-color: rgb(143, 240, 164);\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	background-color: rgb(255, 190, 111);\n"
"	border-radius: 10px;\n"
"}\n"
"")
		self.MenuBase.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.MenuBase.setFrameShadow(QtWidgets.QFrame.Raised)
		self.MenuBase.setObjectName("MenuBase")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.MenuBase)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.DescryptorsFrame = QtWidgets.QFrame(self.MenuBase)
		self.DescryptorsFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.DescryptorsFrame.setStyleSheet("")
		self.DescryptorsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.DescryptorsFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.DescryptorsFrame.setLineWidth(1)
		self.DescryptorsFrame.setMidLineWidth(0)
		self.DescryptorsFrame.setObjectName("DescryptorsFrame")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DescryptorsFrame)
		self.verticalLayout_4.setSpacing(5)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.nameEncryptors_2 = QtWidgets.QLabel(self.DescryptorsFrame)
		self.nameEncryptors_2.setMaximumSize(QtCore.QSize(16777215, 50))
		font = QtGui.QFont()
		font.setFamily("C059")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.nameEncryptors_2.setFont(font)
		self.nameEncryptors_2.setObjectName("nameEncryptors_2")
		self.verticalLayout_4.addWidget(self.nameEncryptors_2)
		self.bReplaceOneLetter_2 = QtWidgets.QPushButton(self.DescryptorsFrame)
		self.bReplaceOneLetter_2.setMinimumSize(QtCore.QSize(0, 40))
		self.bReplaceOneLetter_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.bReplaceOneLetter_2.setObjectName("bReplaceOneLetter_2")
		self.verticalLayout_4.addWidget(self.bReplaceOneLetter_2)
		self.bVigenere_2 = QtWidgets.QPushButton(self.DescryptorsFrame)
		self.bVigenere_2.setMinimumSize(QtCore.QSize(0, 40))
		self.bVigenere_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.bVigenere_2.setObjectName("bVigenere_2")
		self.verticalLayout_4.addWidget(self.bVigenere_2)
		self.bEnigma_2 = QtWidgets.QPushButton(self.DescryptorsFrame)
		self.bEnigma_2.setMinimumSize(QtCore.QSize(0, 40))
		self.bEnigma_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.bEnigma_2.setObjectName("bEnigma_2")
		self.verticalLayout_4.addWidget(self.bEnigma_2)
		self.verticalLayout_4.setStretch(1, 20)
		self.verticalLayout_4.setStretch(2, 20)
		self.verticalLayout_4.setStretch(3, 20)
		self.verticalLayout_5.addWidget(self.DescryptorsFrame)
		self.EncryptorsFrame = QtWidgets.QFrame(self.MenuBase)
		self.EncryptorsFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.EncryptorsFrame.setStyleSheet("")
		self.EncryptorsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.EncryptorsFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.EncryptorsFrame.setLineWidth(1)
		self.EncryptorsFrame.setMidLineWidth(0)
		self.EncryptorsFrame.setObjectName("EncryptorsFrame")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.EncryptorsFrame)
		self.verticalLayout_2.setSpacing(5)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.nameEncryptors = QtWidgets.QLabel(self.EncryptorsFrame)
		self.nameEncryptors.setMaximumSize(QtCore.QSize(16777215, 50))
		font = QtGui.QFont()
		font.setFamily("C059")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.nameEncryptors.setFont(font)
		self.nameEncryptors.setObjectName("nameEncryptors")
		self.verticalLayout_2.addWidget(self.nameEncryptors)
		self.bReplaceOneLetter = QtWidgets.QPushButton(self.EncryptorsFrame)
		self.bReplaceOneLetter.setMinimumSize(QtCore.QSize(0, 40))
		self.bReplaceOneLetter.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.bReplaceOneLetter.setObjectName("bReplaceOneLetter")
		self.verticalLayout_2.addWidget(self.bReplaceOneLetter)
		self.bVigenere = QtWidgets.QPushButton(self.EncryptorsFrame)
		self.bVigenere.setMinimumSize(QtCore.QSize(0, 40))
		self.bVigenere.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.bVigenere.setObjectName("bVigenere")
		self.verticalLayout_2.addWidget(self.bVigenere)
		self.bEnigma = QtWidgets.QPushButton(self.EncryptorsFrame)
		self.bEnigma.setMinimumSize(QtCore.QSize(0, 40))
		self.bEnigma.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.bEnigma.setObjectName("bEnigma")
		self.verticalLayout_2.addWidget(self.bEnigma)
		self.verticalLayout_2.setStretch(1, 20)
		self.verticalLayout_2.setStretch(2, 20)
		self.verticalLayout_2.setStretch(3, 20)
		self.verticalLayout_5.addWidget(self.EncryptorsFrame)
		self.verticalLayout_3.addWidget(self.MenuBase)
		self.verticalLayout.addWidget(self.footerMenu_content)
		footerMenu.setCentralWidget(self.footerMenu_central)

		self.retranslateUi(footerMenu)
		QtCore.QMetaObject.connectSlotsByName(footerMenu)

	def retranslateUi(self, footerMenu):
		_translate = QtCore.QCoreApplication.translate
		footerMenu.setWindowTitle(_translate("footerMenu", "Cryptography"))
		self.flText.setText(_translate("footerMenu", "Cryptography "))
		self.nameEncryptors_2.setText(_translate("footerMenu", "Descryptors:"))
		self.bReplaceOneLetter_2.setText(_translate("footerMenu", "ReplaceOneLetter"))
		self.bVigenere_2.setText(_translate("footerMenu", "Vigenere"))
		self.bEnigma_2.setText(_translate("footerMenu", "Enigma"))
		self.nameEncryptors.setText(_translate("footerMenu", "Encryptors:"))
		self.bReplaceOneLetter.setText(_translate("footerMenu", "ReplaceOneLetter"))
		self.bVigenere.setText(_translate("footerMenu", "Vigenere"))
		self.bEnigma.setText(_translate("footerMenu", "Enigma"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	footerMenu = QtWidgets.QMainWindow()
	ui = Ui_footerMenu()
	ui.setupUi(footerMenu)
	footerMenu.show()
	sys.exit(app.exec_())