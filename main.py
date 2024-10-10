import statistics
from scipy.stats import skew 

class CalculoEstatistica:
    
    def __init__(self, lista):
        self.lista = lista
        
    def media(self):
        return sum(self.lista) / len(self.lista)
    
    def mediana(self):
        ListaCopiar = self.lista #evitar que mude as características da
        ordenacaoLista = sorted(ListaCopiar)
        quantidadenaLista = len(self.lista)
        numero_central = quantidadenaLista // 2 
        
        if (quantidadenaLista % 2) == 0:
            # Quando o número de elementos é par
            return (ordenacaoLista[numero_central - 1] + ordenacaoLista[numero_central]) / 2
        else:
            # Quando o número de elementos é ímpar
            return ordenacaoLista[numero_central]
    
    def moda(self):
        ListaCopiar2 = self.lista
        ordenacaoLista2 = sorted(ListaCopiar2)
        return statistics.mode(ordenacaoLista2)
    
    def varianca(self):
        return statistics.variance(self.lista)
    
    def desvio_padrao(self):
        return statistics.stdev(self.lista)
    
    def coeficiente_assimetria(self):
        return skew(self.lista)

listaNumeros = [2, 2, 2 , 6, 8, 9, 60, 70, 56]

calculos = CalculoEstatistica(listaNumeros)

print("O valor da média da lista é ", calculos.media())
print("O valor da mediana da lista é ", calculos.mediana())
print("O valor da moda da lista é ", calculos.moda())
print("O valor da variancia da lista é ", calculos.varianca())
print("O valor do Desvio Padrão da lista é ", calculos.desvio_padrao())
print("O valor da Assimetria é ", calculos.coeficiente_assimetria())


