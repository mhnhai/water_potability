from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QLabel,QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout
from fetch_model import *


class MainWindow(QMainWindow):
    properties: [str] = ["ph", "Hardness", "Solids", "Chloramines", "Sulfate", "Conductivity", "Organic Carbon", "Trihalomethanes", "Turbidity"]
    labels = []
    inputs = []
    container = []
    result_label: QLabel
    calculate_button: QPushButton

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Water Potability")

        self.result_label = QLabel("Result will be shown here.")
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setFixedWidth(90)
        self.calculate_button.pressed.connect(self.on_calculate_clicked)

        for i in range(len(self.properties)):
            label = QLabel(self.properties[i])
            label.setFixedHeight(20)
            self.labels.append(label)

            line_edit = QLineEdit()
            line_edit.setFixedWidth(90)
            self.inputs.append(line_edit)
            #self.inputs[i].textChanged.connect(self.inputs[i].setText)

            ctn = QVBoxLayout()
            ctn.addWidget(self.labels[i])
            ctn.addWidget(self.inputs[i])
            self.container.append(ctn)


        layoutInputs = QGridLayout()
        layoutInputs.setSpacing(10)
        for i in range(len(self.container)):
            layoutInputs.addLayout(self.container[i], int(i/3), i % 3)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layoutInputs)
        mainLayout.addWidget(self.calculate_button)
        mainLayout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(mainLayout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def on_calculate_clicked(self) -> None:
        try:
            floats = []
            for ip in self.inputs:
                txt = ip.text()
                if txt == "":
                    floats.append(0.0)
                else:
                    floats.append(float(txt))
            print("data is: ", floats)
            print(get_result([floats]))
            if get_result([floats]) == True:
                self.result_label.setText("This water is potable.")
                self.result_label.setStyleSheet("color: black;")
            else:
                self.result_label.setText("This water is NOT potable.")
                self.result_label.setStyleSheet("color: red;")
        except:
            self.result_label.setText("Error number formatting.")
            self.result_label.setStyleSheet("color: orange;")



app = QApplication([])

window = MainWindow()
#window.setFixedSize(850, 130)
window.show()

app.exec()
