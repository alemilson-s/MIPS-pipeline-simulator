class Dado:
    """
    Classe para criação de dados
    """

    def __init__(self, bits):
        """
        Construtor da classe
        :param bits: Representa os 32 bits de um dado
        """
        self.bits = []  # Lista que representa os bits do dado, o bit na posição 0 é o mais significativo
        if type(bits) == list and len(bits) == 32:
            self.bits = bits.copy()
        elif len(bits) == 32:
            for valor in bits:
                self.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    def getDado(self):
        """
        Retorna uma lista com todos os 32 bits do dado
        :return: Lista com 32 bits do dado
        """
        return self.bits

    def setDado(self, bits):
        """
         Método para alterar os 32 bits da lista(bits) representando os bits de um dado
         :param bits: String ou lista representando 32 bits
         :return: Não há retorno
        """
        if type(bits) == list and len(bits) == 32:
            self.bits = bits.copy()
        elif len(bits) == 32:
            self.bits.clear()
            for valor in bits:
                self.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")


class MemoriaDeDados:
    """
    Classe representando a memória de dados
    """

    dados: map = {}  # Dicionário que vincula endereços de memória a dados
    address = ""  #
    writeData = ""
    readData = ""

    @classmethod
    def inicializar_memoria(cls):
        """
        Método para instanciar um novo dado e vincula-la a um endereço de memória
        :param bits: String representando os 32 bits do dado
        :return: Não há retorno
        """
        cls.address = "00000000000000000000000000000000"
        cls.writeData = "00000000000000000000000000000000"
        cls.readData = "00000000000000000000000000000000"

        endereco_atual = "00000000000000000000000000000000"  # Endereço ao qual um novo dado será vinculado
        quatro_bytes = "000001000000000000000000000000000"  # Variável para auxiliar no cálculo do endereço do
        # próximo dado

        # invertendo os bits do dado para manter o padrão
        vai_um: bool = False  # Variável para auxiliar na soma binária de endereco_atual com quatro_bytes
        while endereco_atual != "00000000000010000000000000000000":
            print(endereco_atual[::-1])
            cls.dados[endereco_atual[::-1]] = Dado("00000000000000000000000000000000")  # Instanciando um novo dado e
            # invertendo os bits do dado para manter o padrão
            for indice, valor in enumerate(endereco_atual):
                if valor == '0' and quatro_bytes.__getitem__(indice) == '0' and not vai_um:
                    aux = list(endereco_atual)
                    aux[indice] = '0'
                    endereco_atual = "".join(aux)
                    vai_um = False
                elif valor == '1' and quatro_bytes.__getitem__(indice) == '0' and not vai_um:
                    aux = list(endereco_atual)
                    aux[indice] = '1'
                    endereco_atual = "".join(aux)
                    vai_um = False
                elif valor == '1' and quatro_bytes.__getitem__(indice) == '1' and not vai_um:
                    aux = list(endereco_atual)
                    aux[indice] = '0'
                    endereco_atual = "".join(aux)
                    vai_um = True
                elif valor == '0' and quatro_bytes.__getitem__(indice) == '1' and not vai_um:
                    aux = list(endereco_atual)
                    aux[indice] = '1'
                    endereco_atual = "".join(aux)
                    vai_um = False
                elif valor == '0' and quatro_bytes.__getitem__(indice) == '0' and vai_um:
                    aux = list(endereco_atual)
                    aux[indice] = '1'
                    endereco_atual = "".join(aux)
                    vai_um = False
                elif valor == '1' and quatro_bytes.__getitem__(indice) == '0' and vai_um:
                    aux = list(endereco_atual)
                    aux[indice] = '0'
                    endereco_atual = "".join(aux)
                    vai_um = True
                elif valor == '1' and quatro_bytes.__getitem__(indice) == '1' and vai_um:
                    aux = list(endereco_atual)
                    aux[indice] = '1'
                    endereco_atual = "".join(aux)
                    vai_um = True
                elif valor == '0' and quatro_bytes.__getitem__(indice) == '1' and vai_um:
                    aux = list(endereco_atual)
                    aux[indice] = '0'
                    endereco_atual = "".join(aux)
                    vai_um = True

    @classmethod
    def get(cls):
        """
        Método para retornar um dado recebido seu endereço
        """
        cls.readData = cls.dados[cls.address].getDado()
        return cls.readData

    @classmethod
    def set(cls):
        """
        Método para alterar o conteudo de um endereco de memoria
        """
        cls.dados[cls.address].setDado(cls.writeData)

    @classmethod
    def setAddress(cls, address):
        if type(address) == str and len(address) == 32:
            cls.address = str(address)
        elif len(address) == 32:
            cls.address = ""
            for valor in address:
                cls.address = cls.address + cls.address.join(valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def setWriteDate(cls, writeData):
        if type(writeData) == str and len(writeData) == 32:
            cls.writeData = str(writeData)
        elif len(writeData) == 32:
            cls.writeData = ""
            for valor in writeData:
                cls.writeData = cls.writeData + cls.writeData.join(valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

# MemoriaDeDados.inicializar_memoria()
# MemoriaDeDados.setAddress("00000000000000000000111110000000")
# print(MemoriaDeDados.get())
# MemoriaDeDados.setWriteDate("00000111000000000000111110111111")
# MemoriaDeDados.set()
# print(MemoriaDeDados.get())
