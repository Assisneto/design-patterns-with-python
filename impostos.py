# # -*- coding: UTF-8 -*-
# impostos.py
from abc import ABCMeta, abstractmethod

class Template_de_imposto_condicional(object):
        __metaclass__ = ABCMeta

        def calcula(self,orcamento):
            if self.condicao_maxima(orcamento):
                return self.imposto_maximo(orcamento)
            else:
                 return self.imposto_minimo(orcamento)
        
        @abstractmethod
        def condicao_maxima(self,orcamento):
            pass
        
        @abstractmethod
        def imposto_maximo(self,orcamento):
            pass
        
        @abstractmethod
        def imposto_minimo(self,orcamento):
            pass

class IKCV(Template_de_imposto_condicional):

    def condicao_maxima(self,orcamento):
        
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)
  
    def imposto_maximo(self,orcamento):
        return orcamento.valor * 0.10
    def imposto_minimo(self,orcamento):
        return orcamento.valor * 0.06
      
    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if(item.valor > 100):
                return True
        return False

class ICPP(Template_de_imposto_condicional):
    
   
    def condicao_maxima(self,orcamento):
       return orcamento.valor > 500

    def imposto_maximo(self,orcamento):
        return orcamento.valor * 0.07

    def imposto_minimo(self,orcamento):
        return orcamento.valor * 0.05

class ICMS(object):
    def calcula(self,orcamento):
        return orcamento.valor * 0.1

class ISS(object):
    def calcula(self,orcamento):
        return orcamento.valor * 0.06

