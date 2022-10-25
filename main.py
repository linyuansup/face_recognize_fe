import sys
sys.path.append("")
from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet, export_theme

import init_win

if __name__ == '__main__':

    extra = {
        'font_size': '10px'
    }
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    apply_stylesheet(app, theme='light_pink.xml', extra=extra)
    ui = init_win.Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Child = QDialog()
    # child = test.Ui_Dialog()
    # child.setupUi(Child)

    sys.exit(app.exec_())


