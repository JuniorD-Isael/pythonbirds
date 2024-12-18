class Pessoa:
    # Atributo de classe
    olhos = 2
    def __init__(self, *filhos,nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        # Atributo Complexo
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

    # Atributo Dinamico
    isael.sobrenome = "Junior"
    del isael.filhos

    # Os atributos de instância ficam presente no atributo especial __dict__

    Pessoa.olhos = 3
    isael.olhos = 1

    print(isael.__dict__)
    print(caio.__dict__)
    print(id(Pessoa.olhos))
    print(id(isael.olhos))
    print(id(caio.olhos))
    del isael.olhos
    print(isael.__dict__)