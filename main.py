from PyQt5 import uic, QtWidgets
import numpy as np # linear algebra
import pandas as pd
import sys
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import cdist
from matplotlib import pyplot as plt
from scipy.spatial import distance
import math

######################%matplotlib inline


np.set_printoptions(precision=5, suppress=True)  # suppress scientific float notation
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

qtCreatorFile = "telaprincipal.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Trabalho Mineiração de Dados")

        # inicia comandos invisiveis
        self.metodocbx.setVisible(0)
        self.label_2.setVisible(0)
        self.printarbtn.setVisible(0)

        # Actions
        self.escolherbtn.clicked.connect(self.getCSV)


    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir Arquivo", '.', "(*.csv)")

        if filePath != "":
            print("Dirección", filePath)  # Opcional imprimir la dirección del archivo
            self.df = pd.read_csv(str(filePath), index_col=[0])
            self.caminhotxt.setText(str(filePath)) #escreve o caminho no campo de informar o texto
            self.metodocbx.setVisible(1)
            self.label_2.setVisible(1)
            self.printarbtn.setVisible(1)

            X = self.df.values()
            self.single_link = linkage(self.X, 'single')

            # calculate full dendrogram
            plt.figure(figsize=(25, 10))
            plt.title('Hierarchical Clustering Dendrogram')
            plt.xlabel('sample index')
            plt.ylabel('distance')
            dendrogram(
                self.single_link,
                leaf_rotation=90.,  # rotates the x axis labels
                leaf_font_size=8.,  # font size for the x axis labels
                color_threshold=.6
            )
            plt.show()

    # fim do def plotar
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    app.aboutToQuit.connect(app.deleteLater)  # if using IPython Console
