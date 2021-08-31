## 1 - Criação da Classe e banco de dados
import _sqlite3
banco = _sqlite3.connect('Chefe_grupo.db')
class Chefe_Grupo:
## 2 - Inserção de dados para cadastro do chefe
    opcao = 'y'
    cod_chefe = 0
    cod_chefe = cod_chefe + 1
    nome = str(input("Digite o nome: "))
    email = str(input("Digite o e-mail: "))
    cpf = int(input("Digite o cpf: "))
    setor = str(input("Digite o setor: "))
## 3- Declaração das variáveis
    def __init__(self, cod_chefe, nome, email, cpf, setor):
        self.cod_chefe = cod_chefe
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.setor = setor
## 4 - Condição para alterar dados ##
    print("\n")
    print("Deseja alterar os dados? y / n ")
    opcao = str(input())
    if (opcao == 'y'):
        nome = str(input("Digite o nome: "))
        email = str(input("Digite o e-mail: "))
        cpf = int(input("Digite o cpf: "))
        setor = str(input("Digite o setor: "))
        print("\n")
        print("Cadastro alterado!")
    else:
        print("Cadastro realizado!")
        print("\n")
## 5 - Saída de dados
        print("Cod_Chefe: ", cod_chefe)
        print("Nome: ", nome)
        print("Email: ", email)
        print("Cpf: ", cpf)
        print("Setor: ", setor)























