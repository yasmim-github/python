import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

print("rodando")

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello world')
        self.setWindowIcon(QIcon('snk.png'))
        self.resize(500,350)

        layout = QVBoxLayout()
        self.setLayout(layout)

        print("class rodando")

        # widgets
        self.inputField = QLineEdit()
        button = QPushButton('&Say hello', clicked=self.sayHello)
        # button.clicked.connect(self.sayHello) <-alternative to clicked=self.sayHello
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)
    
    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello {0}'.format(inputText))


app = QApplication([sys.argv])
print("app rodando")
app.setStyleSheet('''
    QWidget {
        font-size: 25px;
    }
                  
    QPushButton {
        font-size: 20px;
    }
                  ''')

window = MyApp()
print("window rodando")
window.show()

sys.exit(app.exec())