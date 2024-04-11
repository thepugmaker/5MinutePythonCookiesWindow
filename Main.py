import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget 

app = QApplication([])

window = QWidget()
window.setWindowTitle("Window")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h5>Give me your cookies >:(</h5>", parent=window)
helloMsg.move(500, 150)

window.show()
sys.exit(app.exec())