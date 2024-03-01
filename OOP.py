class Carros:
    def __init__(self, nome, marca, ano, km, categoria):
        self.Nome = nome
        self.Marca = marca
        self.Ano = ano
        self.km = km
        self.Categoria = categoria
    def revisao(self):
        kilometragem = self.km
        revi = int(kilometragem/10000)
        if revi >1:
            print(f'O carro ja fez {revi} revisoes.')
        elif revi == 1:
            print(f'O carro so fez {revi} revisao.')
        else:
            print('O carro ainda nao fez revisao.')
class tv:
    def __init__(self, status:bool, canal:str, tamanho:int, volume:int):
        self.tamanho = tamanho
        self.status = status
        self.canal = canal
        self.tamanho = tamanho
        self.volume = volume
    def ligar(self):
        if self.status == True:
            print('A televisao ja esta ligada!')
        else:
            self.status = True
    def mudar_canal(self, canal:str):
        if self.status == True:
            if self.canal == canal:
                print('A televisao ja esta nesse canal.')
            else:
                self.canal = canal
        else:
            print('A televisao esta desligada, ligue primeiro para poder mudar de canal.')
    def aumentar_volume(self):
        if self.status == True:
            if self.volume <100:
                self.volume += 1
            else:
                print("A televisao ja esta no volume maximo.")
        else:
            print('A televisao esta desligada, ligue primeiro para poder aumentar o volume.')
    def abaixar_volume(self):
        if self.status == True:
            if self.volume>0:
                self.volume-=1
            else:
                print("A televisao ja esta no volume minimo")
        else:
            print('A televisao esta desligada, ligue primeiro para poder abaixar o volume.')
    def desligar(self):
        if self.status == False:
            print("A televisao ja esta desligada")
        else:
            self.status = False
tv_quarto = tv(True,'Globo', 30, 23)
tv_quarto.abaixar_volume()
tv_quarto.desligar()
print(tv_quarto.status)
