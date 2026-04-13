class Paciente:  # Classe No
    def __init__(self, nome, cpf, idade, urgencia):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.urgencia = urgencia
        self.proximo = None

    def mostrar_no(self) -> int:
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        print(f"Nível de Urgência: {self.urgencia}")
        if self.urgencia == 4:
            print("Imediato")
        elif self.urgencia == 3:
            print("Muito Urgente")
        elif self.urgencia == 2:
            print("Urgente")
        elif self.urgencia == 1:
            print("Pouco Urgente")
        elif self.urgencia == 0:
            print("Não Urgente")
        return 1
