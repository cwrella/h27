import json
from PyQt6 import QtWidgets
from test2 import Ui_MainWindow
import requests


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.method)

    def method(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        if response.status_code == 200:
            data = response.json()
            self.textBrowser.setPlainText(json.dumps(data, indent=4))

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()