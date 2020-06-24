from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication
from PyQt5.QtGui import QFont, QIcon
from planner.TrajectoryController import TrajectoryController
from online.OnlineController import OnlineController
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.font = QFont("Microsoft YaHei")
        self.setFont(self.font)
        self.setUI()

    def setUI(self):
        self.setWindowIcon(QIcon('./planner/pic/dig.jpg'))
        self.setWindowTitle("Tuning Software for ATPGlobal")

        self.tab = QTabWidget()
        self.trajectory = TrajectoryController()
        self.online = OnlineController()
        self.tab.addTab(self.online, "Online")
        self.tab.addTab(self.trajectory, "Trajectory")
        self.setCentralWidget(self.tab)
        self.showMaximized()


if __name__=="__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

