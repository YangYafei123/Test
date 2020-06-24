import sys, os
if hasattr(sys, 'frozen'):
   os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication


class MainController(MainWindow):
    def __init__(self):
        super(MainController, self).__init__()

    def closeEvent(self, *args, **kwargs):
        '''
        TODO: 关闭所有线程池的线程，必须要，哈哈哈哈
        :param args:
        :param kwargs:
        :return:
        '''
        self.online.close()
        self.close()


if __name__=="__main__":
    app = QApplication(sys.argv)
    mainController = MainController()
    mainController.show()
    sys.exit(app.exec_())
