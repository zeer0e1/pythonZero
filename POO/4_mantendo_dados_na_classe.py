class Camera:
    def __init__(self,nome,filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return
        
        print(f'{self.nome} está filmando')
        self.filmando = True
    
    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando')
            return
        
        print(f'{self.nome} esta parando de filmar')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} n pode fotografar enquanto filma')
            return
        
        print(f'{self.nome} fotografou')

c1 = Camera('Cannon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()