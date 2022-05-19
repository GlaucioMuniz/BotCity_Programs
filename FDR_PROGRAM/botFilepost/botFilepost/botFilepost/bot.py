from PyQt5 import Qt, QtCore, QtWidgets
from botcity.core import DesktopBot
import psutil
from PyQt5.QtWidgets import QMessageBox
import sys
from PyQt5.QtWidgets import *

class Bot(DesktopBot):

    def action(self, execution=None):

        try:

            #Software de teste
            self.execute(r"C:\programa1\programa1.lnk")
            self.wait(5000)
            #Software filepost
            self.execute(r"C:\programa2\programa2.lnk")
            self.wait(5000)
            #Camera 1
            self.execute(r"C:\programa3\programa3.lnk")
            self.wait(5000)
            # Camera 1
            self.execute(r"C:\programa4\programa4.lnk")
            self.wait(5000)
            # Sunwoda Software
            #self.execute(r"C:\programa5\programa5.lnk")
            #self.wait(5000)

        except FileNotFoundError:
            self.show_warning_messagebox()
            quit()

        bool1 = "CMES_FilePost.X1653.exe" in (i.name() for i in psutil.process_iter())
        bool2 = "HawkvisViewer.exe" in (i.name() for i in psutil.process_iter())
        bool3 = "HawkvisViewer.exe" in (i.name() for i in psutil.process_iter())
        bool4 = "WADB.exe" in (i.name() for i in psutil.process_iter())


        if (bool1 & bool2 & bool3 & bool4):

            self.show_info_messagebox()

        else:

            self.show_critical_messagebox()

    def show_info_messagebox(self):

        # create pyqt5 app
        app = QApplication(sys.argv)
        w = QtWidgets.QWidget()

        #Destacar Mensagem de aviso.
        w.setWindowFlags(w.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("OK, INICIAR TESTES")

        # setting Message box window title
        msg.setWindowTitle("INFORMAÇÃO")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        msg.exec_()

    def show_critical_messagebox(self):

        # create pyqt5 app
        app = QApplication(sys.argv)
        w = QtWidgets.QWidget()

        # Destacar Mensagem de aviso.
        w.setWindowFlags(w.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("NOK, NÃO INICIAR TESTES")

        # setting Message box window title
        msg.setWindowTitle("AVISO:VERIFICAR")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        msg.exec_()

    def show_warning_messagebox(self):

        # create pyqt5 app
        app = QApplication(sys.argv)
        w = QtWidgets.QWidget()

        # Destacar Mensagem de aviso.
        w.setWindowFlags(w.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        # setting message for Message Box
        msg.setText("Caminho da pasta ou arquivo inválido")

        # setting Message box window title
        msg.setWindowTitle("AVISO:VERIFICAR")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        msg.exec_()

    #def not_found(self, label):
    #    print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

