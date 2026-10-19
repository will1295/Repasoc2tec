import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication,QMainWindow,QVBoxLayout,QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejemplo de uso de matplotlib')
        self.resize(600,400)
        df = pd.read_csv('inventario.csv')
        self.figura = Figure(figsize=(5,3))
        self.canvas = FigureCanvas(self.figura)

        ax = self.figura.add_subplot(111)
        ax.scatter(df['Stock'],df['Precio'],color='blue')
        ax.set_xlabel("Stock")
        ax.set_ylabel("Precio")
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec_())