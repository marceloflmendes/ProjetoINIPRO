from PyQt5 import uic, QtWidgets
import pymysql

banco = pymysql.connect(
    host="localhost",
    user="root",
    passwd=""
)


def cadastrar():
    cursor = banco.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS plano_saude")
    cursor.execute("USE plano_saude")

    cursor.execute("CREATE TABLE IF NOT EXISTS cliente (nome VARCHAR(255),"
                   "cpf VARCHAR(20) PRIMARY KEY,"
                   "rg VARCHAR(20),"
                   "nascimento VARCHAR(20),"
                   "endereço VARCHAR(255),"
                   "email VARCHAR(255),"
                   "telefone VARCHAR(20),"
                   "plano VARCHAR(255),"
                   "tipo VARCHAR(255),"
                   "corretor VARCHAR(255),"
                   "valor VARCHAR(20),"
                   "escritorio VARCHAR(255),"
                   "vencimento VARCHAR(20))")
    # ENTRADA DOS VALORES

    nome = formulario.lineEdit.text()
    cpf = formulario.lineEdit_3.text()
    rg = formulario.lineEdit_6.text()
    nascimento = formulario.dateEdit.text()
    endereço = formulario.lineEdit_4.text()
    email = formulario.lineEdit_5.text()
    telefone = formulario.lineEdit_2.text()
    plano = formulario.lineEdit_7.text()

    if formulario.radioButton.isChecked():
        tipo = 'Enfermaria'
    elif formulario.radioButton_2.isChecked():
        tipo = 'Apartamento'
    else:
        tipo = 'Odontológico'
    corretor = formulario.lineEdit_9.text()
    valor = formulario.lineEdit_8.text()
    escritorio = formulario.lineEdit_10.text()
    venc = formulario.lineEdit_11.text()

    # Instruções Sql
    try:
        com_sql = "INSERT INTO cliente (nome, cpf, rg, nascimento, endereço, email, telefone, plano, corretor, valor, escritorio, venc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(nome), str(cpf), str(rg), str(nascimento), str(endereço), str(email), str(telefone), str(plano),str(corretor), str(valor), str(escritorio), str(venc))
        cursor.execute(com_sql , dados)
        banco.commit()
    except:
        print('Erro aqui')
    else:
        print('Normal')


app = QtWidgets.QApplication([])
formulario = uic.loadUi('projeto.ui')

formulario.pushButton.clicked.connect(cadastrar)

formulario.show()
app.exec()
