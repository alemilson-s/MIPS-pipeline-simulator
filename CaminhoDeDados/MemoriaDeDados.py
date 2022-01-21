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

    @classmethod
    def inicializar_memoria(cls):
        """
        Método para instanciar um novo dado e vincula-la a um endereço de memória
        :param bits: String representando os 32 bits do dado
        :return: Não há retorno
        """
        endereco_atual = "00000000000000000000000000000000"  # Endereço ao qual um novo dado será vinculado
        quatro_bytes = "000001000000000000000000000000000"  # Variável para auxiliar no cálculo do endereço do
        # próximo dado

        # invertendo os bits do dado para manter o padrão
        vai_um: bool = False  # Variável para auxiliar na soma binária de endereco_atual com quatro_bytes
        while endereco_atual != "00000000000010000000000000000000":
            # print(endereco_atual[::-1])
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
    def get(cls, endereco):
        """
        Método para retornar um dado recebido seu endereço
        :param endereco: Endereço de um dado
        :return: dado vinculado ao endereço
        """
        return cls.dados[endereco].getDado()

    @classmethod
    def set(cls, endereco, dado):
        """
        Método para alterar o conteudo de um endereco de memoria
        :param endereco: Representa um endereco de memoria
        :param dado: Dado que sera escrito no endereco de memoria
        """
        cls.dados[endereco].setDado(dado)


MemoriaDeDados.inicializar_memoria()
MemoriaDeDados.set("00000000000000000000000001100000", "00000011010000000101010101010111")
print(MemoriaDeDados.get("00000000000000000000000001100000"))
print(MemoriaDeDados.get("00000000000000000000111111100000"))
MemoriaDeDados.set("00000000000000000000111111100000", "11111111111111111111111111111111")
print(MemoriaDeDados.get("00000000000000000000111111100000"))
