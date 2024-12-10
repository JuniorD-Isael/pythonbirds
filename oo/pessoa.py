class Pessoa:
    # Metodo

    def __init__(self, nome=None, idade=31):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f"Olá! {id(self)}"

    # Atributos de dado

if __name__ == '__main__':
    p = Pessoa("Isael")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Junior"
    print(p.nome)
    print(p.idade)
