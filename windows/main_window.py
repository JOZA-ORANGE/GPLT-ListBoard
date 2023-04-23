from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem, QProgressBar, QAbstractItemView, QMainWindow, QMenu

from ui.ui_MainWindow import Ui_MainWindow
import function.requestApi as requestApi
import stylesheet.css as css

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 载入MainWindow.ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.updateTeamRank()

        # 允许右键产生子菜单
        self.ui.tableWidget_teamRank.setContextMenuPolicy(Qt.CustomContextMenu)
        # 右键菜单
        self.ui.tableWidget_teamRank.customContextMenuRequested.connect(self.tableWidget_teamRank_menu)

    # 刷新队伍排名
    def updateTeamRank(self):
        score_teams = requestApi.getBoard('teams')
        score_teams_sorted = sorted(score_teams.items(), key=lambda x: x[1]['tScore'], reverse=True)
        # 清空表格内容
        self.ui.tableWidget_teamRank.setRowCount(0)
        #
        self.ui.tableWidget_teamRank.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # 设置不可编辑
        self.ui.tableWidget_teamRank.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        # 单选模式
        self.ui.tableWidget_teamRank.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        # 整行选择
        self.ui.tableWidget_teamRank.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        for i in range(len(score_teams_sorted)):
            self.ui.tableWidget_teamRank.insertRow(i)
            self.ui.tableWidget_teamRank.setColumnWidth(4,10)
            self.ui.tableWidget_teamRank.setToolTip(score_teams_sorted[i][1]['_id'])
            item = QTableWidgetItem()
            item.setText("[" + score_teams_sorted[i][1]['schoolShortname'].upper() + "] " + score_teams_sorted[i][1]['name'])
            self.ui.tableWidget_teamRank.setItem(i, 0, item)

            # 基础级
            progress = QProgressBar()
            progress.setStyleSheet(css.s1+css.s2)
            progress.setRange(0,1000)
            if score_teams_sorted[i][1]['s'][0][0] > progress.maximum():
                value = progress.maximum()
            else:
                value = score_teams_sorted[i][1]['s'][0][0]
            progress.setValue(value)
            if not bool(score_teams_sorted[i][1]['s'][0][1]):
                progress.setStyleSheet(css.s1 + css.s_d)
            progress.setFormat("%s / %s" % (progress.value(), progress.maximum()))
            self.ui.tableWidget_teamRank.setCellWidget(i,1,progress)
            # 进阶级
            progress = QProgressBar()
            progress.setStyleSheet(css.s1 + css.s3)
            progress.setRange(0,1000)
            if score_teams_sorted[i][1]['s'][1][0] > progress.maximum():
                value = progress.maximum()
            else:
                value = score_teams_sorted[i][1]['s'][1][0]
            progress.setValue(value)
            if not bool(score_teams_sorted[i][1]['s'][1][1]):
                progress.setStyleSheet(css.s1 + css.s_d)
            progress.setFormat("%s / %s" % (progress.value(), progress.maximum()))
            self.ui.tableWidget_teamRank.setCellWidget(i,2,progress)
            # 登顶级
            progress = QProgressBar()
            progress.setStyleSheet(css.s1+css.s4)
            progress.setRange(0,900)
            if score_teams_sorted[i][1]['s'][2][0] > progress.maximum():
                value = progress.maximum()
            else:
                value = score_teams_sorted[i][1]['s'][2][0]
            progress.setValue(value)
            if not bool(score_teams_sorted[i][1]['s'][2][1]):
                progress.setStyleSheet(css.s1 + css.s_d)
            progress.setFormat("%s / %s" % (progress.value(),progress.maximum()))
            self.ui.tableWidget_teamRank.setCellWidget(i,3,progress)
            item = QTableWidgetItem()
            item.setText(str(score_teams_sorted[i][1]['tScore']))
            self.ui.tableWidget_teamRank.setItem(i, 4, item)

    def tableWidget_teamRank_menu(self,pos):
        row = self.ui.tableWidget_teamRank.currentRow()

        menu = QMenu()
        item1 = menu.addAction(u"详情")
        action = menu.exec_(self.ui.tableWidget_teamRank.mapToGlobal(pos))
        if action == item1:
            print("选中了",row)
