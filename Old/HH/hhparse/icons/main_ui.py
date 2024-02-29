# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextBrowser, QTextEdit,
    QWidget)
import icons.res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 685)
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: JetBrains Mono;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 60, 791, 391))
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.textBrowser.setFont(font1)
        self.textBrowser.setStyleSheet(u"color: white;\n"
"border-radius: 5px;\n"
"border: 2px solid #FFF;\n"
"border-image: url(:/Icons/zayka.png);\n"
"border-width: 0px;")
        self.company_name = QLabel(self.centralwidget)
        self.company_name.setObjectName(u"company_name")
        self.company_name.setGeometry(QRect(10, 10, 321, 41))
        self.company_name.setStyleSheet(u"border-radius: 10px;\n"
"border: 3px solid #FFF;\n"
"background: #000;")
        self.company_name_text = QLabel(self.centralwidget)
        self.company_name_text.setObjectName(u"company_name_text")
        self.company_name_text.setGeometry(QRect(81, 20, 231, 21))
        self.salary_1 = QLabel(self.centralwidget)
        self.salary_1.setObjectName(u"salary_1")
        self.salary_1.setGeometry(QRect(335, 10, 291, 41))
        self.salary_1.setStyleSheet(u"border-radius: 10px;\n"
"border: 3px solid #FFF;\n"
"background: #000;")
        self.weather = QLabel(self.centralwidget)
        self.weather.setObjectName(u"weather")
        self.weather.setGeometry(QRect(630, 10, 161, 41))
        self.weather.setStyleSheet(u"border-radius: 10px;\n"
"border: 3px solid #FFF;\n"
"background: #000;")
        self.salary_text = QLabel(self.centralwidget)
        self.salary_text.setObjectName(u"salary_text")
        self.salary_text.setGeometry(QRect(409, 20, 201, 21))
        self.weather_text = QLabel(self.centralwidget)
        self.weather_text.setObjectName(u"weather_text")
        self.weather_text.setGeometry(QRect(690, 20, 91, 21))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 451, 791, 232))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.edit_text = QTextEdit(self.layoutWidget)
        self.edit_text.setObjectName(u"edit_text")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_text.sizePolicy().hasHeightForWidth())
        self.edit_text.setSizePolicy(sizePolicy)
        self.edit_text.setMinimumSize(QSize(450, 230))
        self.edit_text.setFont(font1)
        self.edit_text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.edit_text.setStyleSheet(u"background-color: #121212;\n"
"border-radius: 5px;\n"
"border: 2px solid #FFF;\n"
"background: #000;")

        self.gridLayout_2.addWidget(self.edit_text, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_send = QPushButton(self.layoutWidget)
        self.btn_send.setObjectName(u"btn_send")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_send.sizePolicy().hasHeightForWidth())
        self.btn_send.setSizePolicy(sizePolicy1)
        self.btn_send.setMinimumSize(QSize(171, 71))
        font2 = QFont()
        font2.setFamilies([u"JetBrains Mono"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.btn_send.setFont(font2)
        self.btn_send.setStyleSheet(u"QPushButton {\n"
"background-color: #121212;\n"
"border-radius: 10px;\n"
"border: 2px solid #FFF;\n"
"background: #000;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #666;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #888;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/Icons/baseline_send_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send.setIcon(icon)
        self.btn_send.setIconSize(QSize(32, 20))

        self.gridLayout.addWidget(self.btn_send, 0, 0, 1, 1)

        self.btn_skip = QPushButton(self.layoutWidget)
        self.btn_skip.setObjectName(u"btn_skip")
        sizePolicy1.setHeightForWidth(self.btn_skip.sizePolicy().hasHeightForWidth())
        self.btn_skip.setSizePolicy(sizePolicy1)
        self.btn_skip.setMinimumSize(QSize(141, 71))
        self.btn_skip.setFont(font2)
        self.btn_skip.setStyleSheet(u"QPushButton {\n"
"background-color: #121212;\n"
"border-radius: 10px;\n"
"border: 2px solid #FFF;\n"
"background: #000;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #666;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #888;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/baseline_not_interested_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_skip.setIcon(icon1)
        self.btn_skip.setIconSize(QSize(18, 29))

        self.gridLayout.addWidget(self.btn_skip, 0, 1, 1, 1)

        self.btn_next = QPushButton(self.layoutWidget)
        self.btn_next.setObjectName(u"btn_next")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy2)
        self.btn_next.setFont(font)
        self.btn_next.setStyleSheet(u"QPushButton {\n"
"background-color: #121212;\n"
"border-radius: 10px;\n"
"border: 2px solid #FFF;\n"
"background: #000;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #666;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #888;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/baseline_navigate_next_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon2)
        self.btn_next.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_next, 1, 0, 1, 1)

        self.btn_prev = QPushButton(self.layoutWidget)
        self.btn_prev.setObjectName(u"btn_prev")
        sizePolicy1.setHeightForWidth(self.btn_prev.sizePolicy().hasHeightForWidth())
        self.btn_prev.setSizePolicy(sizePolicy1)
        self.btn_prev.setFont(font)
        self.btn_prev.setStyleSheet(u"QPushButton {\n"
"background-color: #121212;\n"
"border-radius: 10px;\n"
"border: 2px solid #FFF;\n"
"background: #000;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #666;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #888;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/baseline_chevron_left_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prev.setIcon(icon3)

        self.gridLayout.addWidget(self.btn_prev, 1, 1, 1, 1)

        self.btn_respond = QPushButton(self.layoutWidget)
        self.btn_respond.setObjectName(u"btn_respond")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(168)
        sizePolicy3.setVerticalStretch(200)
        sizePolicy3.setHeightForWidth(self.btn_respond.sizePolicy().hasHeightForWidth())
        self.btn_respond.setSizePolicy(sizePolicy3)
        self.btn_respond.setFont(font2)
        self.btn_respond.setStyleSheet(u"QPushButton {\n"
"background-color: #121212;\n"
"border-radius: 10px;\n"
"border: 2px solid #FFF;\n"
"background: #000;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #666;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #888;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/baseline_reply_all_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_respond.setIcon(icon4)
        self.btn_respond.setIconSize(QSize(31, 23))

        self.gridLayout.addWidget(self.btn_respond, 2, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.layoutWidget.raise_()
        self.textBrowser.raise_()
        self.company_name.raise_()
        self.company_name_text.raise_()
        self.salary_1.raise_()
        self.weather.raise_()
        self.salary_text.raise_()
        self.weather_text.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HHEblya", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'JetBrains Mono'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Waiting for script</p></body></html>", None))
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f:", None))
        self.company_name_text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.salary_1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430:", None))
        self.weather.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430:", None))
        self.salary_text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weather_text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.edit_text.setDocumentTitle("")
        self.edit_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'JetBrains Mono'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.edit_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442...", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.btn_skip.setText(QCoreApplication.translate("MainWindow", u"Skip", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.btn_prev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.btn_respond.setText(QCoreApplication.translate("MainWindow", u"Respond", None))
    # retranslateUi

