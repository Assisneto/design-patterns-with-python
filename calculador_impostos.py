from impostos import *
class Calculador_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        valor = imposto.calcula(orcamento)
        print(valor)


if __name__ == '__main__':
    
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    # adicionando itens ao orçamento
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))
    
    calculador_impostos = Calculador_impostos()
    print ('ISS e ICMS')
    calculador_impostos.realiza_calculo(orcamento, ISS())
    calculador_impostos.realiza_calculo(orcamento, ICMS())

    print("ISS com ICMS") #Composição Decorator
    calculador_impostos.realiza_calculo(orcamento,ISS(ICMS()))

    # cálculo dos novos impostos
    print ('ICPP e IKCV')
    calculador_impostos.realiza_calculo(orcamento, ICPP()) # imprime 25.0
    calculador_impostos.realiza_calculo(orcamento, IKCV()) # imprime 30.0

    print("ICPP com IKCV") 
    calculador_impostos.realiza_calculo(orcamento, ICPP(IKCV()))