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


    # Metodo de classe
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atrubuto_de_classe(cls):
        return f"{cls}: olhos {cls.olhos}"

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    caio = Homem(nome="Caio")
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
    print(isael.metodo_estatico(), isael.metodo_estatico())
    print(caio.nome_e_atrubuto_de_classe())
    print(isael.nome_e_atrubuto_de_classe())
    new_pessoa = Pessoa("Anonimo")
    print(isinstance(new_pessoa, Pessoa))
    print(isinstance(new_pessoa, Homem))

    print(isinstance(caio, Pessoa))
    print(isinstance(caio, Homem))
