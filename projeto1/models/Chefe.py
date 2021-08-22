class Chefe_Grupo:

    nome = str(input("Digite o nome: "))
    email = str(input("Digite o email: "))
    cpf = int(input("Digite o cpf: "))
    setor = str(input("Digite o setor: "))

    def __init__(self, cod_chefe, nome, email, cpf, setor):
        self.cod_chefe = cod_chefe
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.setor = setor

    print("Nome: ", nome)
    print("Email: ", email)
    print("Cpf: ", cpf)
    print("Setor: ", setor)







