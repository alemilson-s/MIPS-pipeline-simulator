class Instrucao:
    """
    Classe para criação de instruções
    """

    def __init__(self, bits):
        """
        Construtor da classe
        :param bits: Representa 32 bits da instrução
        """
        self.bits = []  # Lista que representa os bits da instrução, o bit na posição 0 é o mais significativo
        if type(bits) == list and len(bits) == 32:
            self.bits = bits.copy()
        elif len(bits) == 32:
            self.bits.clear()
            for valor in bits:
                self.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    def getInstrucao(self):
        """
        Retorna uma lista com todos os 32 bits da instrução
        :return: Lista com 32 bits da instrução
        """
        return self.bits


class MemoriaDeInstrucoes:
    """
    Classe representando a memória de instruções
    """
    instrucoes: map = {}  # Dicionário que vincula endereços de memória a instruções
    endereco_atual = "00000000000000000000000000000000"  # Endereço ao qual uma nova instrução será vinculado

    @classmethod
    def inserir_instrucao(cls, bits):
        """
        Método para instanciar uma nova instrução e vincula-la a um endereço de memória
        :param bits: String representando os 32 bits da instrução
        :return: Não há retorno
        """
        quatro_bytes = "000001000000000000000000000000000"  # Variável para auxiliar no cálculo  do endereço da
        # próxima instrução

        cls.instrucoes[cls.endereco_atual[::-1]] = Instrucao(bits)  # Instanciando uma nova instrução e
        # invertendo os bits da instrução para manter o padrão
        vai_um: bool = False  # Variável para auxiliar na soma binária de endereco_atual com quatro_bytes

        for indice, valor in enumerate(cls.endereco_atual):
            if valor == '0' and quatro_bytes.__getitem__(indice) == '0' and not vai_um:
                aux = list(cls.endereco_atual)
                aux[indice] = '0'
                cls.endereco_atual = "".join(aux)
                vai_um = False
            elif valor == '1' and quatro_bytes.__getitem__(indice) == '0' and not vai_um:
                aux = list(cls.endereco_atual)
                aux[indice] = '1'
                cls.endereco_atual = "".join(aux)
                vai_um = False
            elif valor == '1' and quatro_bytes.__getitem__(indice) == '1' and not vai_um:
                aux = list(cls.endereco_atual)
                aux[indice] = '0'
                cls.endereco_atual = "".join(aux)
                vai_um = True
            elif valor == '0' and quatro_bytes.__getitem__(indice) == '1' and not vai_um:
                aux = list(cls.endereco_atual)
                aux[indice] = '1'
                cls.endereco_atual = "".join(aux)
                vai_um = False
            elif valor == '0' and quatro_bytes.__getitem__(indice) == '0' and vai_um:
                aux = list(cls.endereco_atual)
                aux[indice] = '1'
                cls.endereco_atual = "".join(aux)
                vai_um = False
            elif valor == '1' and quatro_bytes.__getitem__(indice) == '0' and vai_um:
                aux = list(cls.endereco_atual)
                aux[indice] = '0'
                cls.endereco_atual = "".join(aux)
                vai_um = True
            elif valor == '1' and quatro_bytes.__getitem__(indice) == '1' and vai_um:
                aux = list(cls.endereco_atual)
                aux[indice] = '1'
                cls.endereco_atual = "".join(aux)
                vai_um = True
            elif valor == '0' and quatro_bytes.__getitem__(indice) == '1' and vai_um:
                aux = list(cls.endereco_atual)
                aux[indice] = '0'
                cls.endereco_atual = "".join(aux)
                vai_um = True

    @classmethod
    def getInstrucao(cls, endereco):
        """
        Método para retornar uma instrução dado seu endereço
        :param endereco: Endereço de uma instrução
        :return: Instrução vinculada ao endereço
        """
        return cls.instrucoes[endereco].getInstrucao()

#
# # Exemplos de utilização da inserção de instruções
# MemoriaDeInstrucoes.inserir_instrucao("00000011010000000101010101010111")
# MemoriaDeInstrucoes.inserir_instrucao("11110011010000000101010101010111")
# MemoriaDeInstrucoes.inserir_instrucao("00000010001100100100000000100000")
# MemoriaDeInstrucoes.inserir_instrucao("00000011010000000101010101010111")
# MemoriaDeInstrucoes.inserir_instrucao("11111111111111111111111111111111")
# MemoriaDeInstrucoes.inserir_instrucao("00000011010000000101010101010111")
# # Exemplo de recuperação de instrução
# print(MemoriaDeInstrucoes.getInstrucao("00000000000000000000000001100000"))
