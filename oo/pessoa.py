class Pessoa:
    def __init__(self,*filhos ,nome = None, idade = 25):
        self.idade = idade
        self.nome = nome
        self.filhos =list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    caio = Pessoa(nome='Caio')
    alguem = Pessoa(caio, nome='Alguem')
    print(Pessoa.cumprimentar(alguem))
    print(id(alguem))
    print(alguem.cumprimentar())
    print(alguem.nome)
    print(alguem.idade)
    for filho in alguem.filhos:
        print(filho.nome)
    alguem.sobrenome= 'santos'
    print(alguem.sobrenome)
    del alguem.filhos
    print(alguem.__dict__)
    print(caio.__dict__)
