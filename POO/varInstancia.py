class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"\nNome: {self.nome}\n Matricula: {self.matricula}\n Escola: {self.escola}"

    def mostrarValores(*objs):
        for obj in objs:
            print(obj)


aluno1 = Estudante("Moisés", 1)
aluno2 = Estudante("Laryssa", 2)
aluno1.escola = "BC"
Estudante.mostrarValores(aluno1, aluno2)