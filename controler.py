from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="db_cadastro_produtos"
)


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()

    categoria = ""

    if formulario.radioButton.isChecked():
        print("Categoria Eletronicos selecionada")
        categoria = "Eletronicos"
    elif formulario.radioButton_2.isChecked():
        print("Categoria Informatica selecionada")
        categoria = "Informatica"
    else:
        print("Categoria Alimentos selecionada")
        categoria = "Alimentos"

    print("Codigo:", linha1)
    print("Descricao:", linha2)
    print("Preco", linha3)
    print("Fabricante", linha4)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco, fabricante, categoria) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

