class Pessoa:
    def __init__(self, *filhos,nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá! {id(self)}"


if __name__ == '__main__':
    caio = Pessoa(nome="Caio")
    isael = Pessoa(caio,nome="Isael")
    print(Pessoa.cumprimentar(isael))
    print(id(isael))
    print(isael.cumprimentar())
    print(isael.nome)
    print(isael.idade)

    for filho in isael.filhos:
        print(filho.nome)
