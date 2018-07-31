# -*- coding: UTF-8 -*-
# calculador_de_descontos.py
from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais

class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhentos_reais(Sem_desconto().calcular())).calcular(orcamento)
    
        return desconto

        # outras possíveis regras aqui

if __name__ == '__main__':

    from orcamento import Orcamento, Item
    from descontos import *
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print ('Desconto calculado : %.2f' % (desconto))
    # imprime 38.5