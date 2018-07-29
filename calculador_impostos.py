from impostos import *
class Calculador_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        return imposto.calcula(orcamento)



if __name__ == '__main__':
    
    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_impostos = Calculador_impostos()
    print(calculador_impostos.realiza_calculo(orcamento, ICMS)) # imprimie 50.0
    print(calculador_impostos.realiza_calculo(orcamento, ISS)) # imprime 30.0