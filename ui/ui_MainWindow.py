# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1000, 600))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget_main = QTabWidget(self.centralwidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        self.tabWidget_main.setGeometry(QRect(0, 0, 1001, 551))
        self.tabWidget_main.setToolTipDuration(-1)
        self.tabWidget_main.setTabPosition(QTabWidget.North)
        self.tab_teamRank = QWidget()
        self.tab_teamRank.setObjectName(u"tab_teamRank")
        self.tableWidget_teamRank = QTableWidget(self.tab_teamRank)
        if (self.tableWidget_teamRank.columnCount() < 5):
            self.tableWidget_teamRank.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_teamRank.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_teamRank.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_teamRank.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_teamRank.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_teamRank.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_teamRank.setObjectName(u"tableWidget_teamRank")
        self.tableWidget_teamRank.setGeometry(QRect(0, 70, 991, 451))
        self.tableWidget_teamRank.setStyleSheet(u"")
        self.tableWidget_teamRank.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_teamRank.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_teamRank.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_teamRank.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_teamRank.verticalHeader().setCascadingSectionResizes(False)
        self.progressBar_time = QProgressBar(self.tab_teamRank)
        self.progressBar_time.setObjectName(u"progressBar_time")
        self.progressBar_time.setGeometry(QRect(890, 0, 100, 10))
        self.progressBar_time.setValue(0)
        self.progressBar_time.setAlignment(Qt.AlignCenter)
        self.progressBar_time.setTextVisible(True)
        self.tabWidget_main.addTab(self.tab_teamRank, "")
        self.tab_Sz = QWidget()
        self.tab_Sz.setObjectName(u"tab_Sz")
        self.tabWidget_main.addTab(self.tab_Sz, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionGithub)

        self.retranslateUi(MainWindow)

        self.tabWidget_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github . . .", None))
#if QT_CONFIG(tooltip)
        self.tabWidget_main.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tabWidget_main.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem = self.tableWidget_teamRank.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u961f\u4f0d\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget_teamRank.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u7ea7", None));
        ___qtablewidgetitem2 = self.tableWidget_teamRank.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u9636\u7ea7", None));
        ___qtablewidgetitem3 = self.tableWidget_teamRank.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u767b\u9876\u7ea7", None));
        ___qtablewidgetitem4 = self.tableWidget_teamRank.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6570", None));
#if QT_CONFIG(statustip)
        self.tableWidget_teamRank.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.progressBar_time.setFormat(QCoreApplication.translate("MainWindow", u"%ms", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_teamRank), QCoreApplication.translate("MainWindow", u"\u56e2\u961f\u6392\u540d", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_Sz), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

