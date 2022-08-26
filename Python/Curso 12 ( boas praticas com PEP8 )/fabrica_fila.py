from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITAIRA

class FabricaFila:
    @staticmethod
    def pega_fila( tipo_fila):
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITAIRA:
            return  FilaPrioritaria()
        else:
            raise NotImplementedError("Tipo de fila não existe...")
