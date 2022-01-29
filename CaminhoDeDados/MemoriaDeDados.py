class Dado:
    """
    Classe para criação de dados
    """

    def __init__(self, bits):
        """
        Construtor da classe: param bits: Representa os 32 bits de um dado
        """
        self.bits = []  # Lista que representa os bits do dado, o bit na posição 0 é o mais significativo
        if type(bits) == list and len(bits) == 32:
            self.bits = bits.copy()
        elif len(bits) == 32:
            for valor in bits:
                self.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    def get_dado(self):
        """
        Retorna uma lista com todos os 32 bits do dado
        return: Lista com 32 bits do dado
        """
        return self.bits

    def set_dado(self, bits):
        """
         Método para alterar os 32 bits da lista(bits) representando os bits de um dado
         param bits: String ou lista representando 32 bits
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

    dados: dict = {}  # Dicionário que vincula endereços de memória a dados
    address = ""  #
    writeData = ""
    readData = ""
    mem_read = False
    mem_write = False

    @classmethod
    def inicializar_memoria(cls):
        """
        Método para instanciar um novo dado e vincula-la a um endereço de memória
        """
        cls.address = "00000000000000000000000000000000"
        cls.writeData = "00000000000000000000000000000000"
        cls.readData = "00000000000000000000000000000000"

        endereco_atual = "00000000000000000000000000000000"  # Endereço ao qual um novo dado será vinculado
        quatro_bytes = "000001000000000000000000000000000"  # Variável para auxiliar no cálculo do endereço do
        # próximo dado

        # invertendo os bits do dado para manter o padrão
        vai_um: bool = False  # Variável para auxiliar na soma binária de endereço atual com quatro ‘bytes’
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
    def read(cls):
        """
        Método para ler o dado de um endereco de memória
        """
        cls.readData = cls.dados[cls.address].get_dado()

    @classmethod
    def write(cls):
        """
        Método para alterar o conteudo de um endereco de memória
        """
        cls.dados[cls.address].set_dado(cls.writeData)

    @classmethod
    def get_read_data(cls):
        """
        Método para retornar dado contido em readData
        """
        return cls.readData

    @classmethod
    def set_address(cls, address):
        if type(address) == str and len(address) == 32:
            cls.address = str(address)
        elif len(address) == 32:
            cls.address = ""
            for valor in address:
                cls.address = cls.address + cls.address.join(valor)
            cls.address = cls.address[::-1]
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def set_write_date(cls, write_data):
        if type(write_data) == str and len(write_data) == 32:
            cls.writeData = write_data
        elif len(write_data) == 32:
            cls.writeData = ""
            for valor in write_data:
                cls.writeData = cls.writeData + cls.writeData.join(valor)
            cls.writeData = cls.writeData[::-1]
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def set_mem_read(cls, sinal):
        cls.mem_read = sinal

    @classmethod
    def set_mem_write(cls, sinal):
        cls.mem_write = sinal

    @classmethod
    def run(cls):
        if cls.mem_write:
            cls.write()
        if cls.mem_read:
            cls.read()

# MemoriaDeDados.inicializar_memoria()
# MemoriaDeDados.set_address(list("00000000000000000000111110000000"[::-1]))
# print(MemoriaDeDados.get_read_data())
# MemoriaDeDados.set_write_date("00000111000000000000111110111111")
# MemoriaDeDados.write()
# MemoriaDeDados.read()
# print(MemoriaDeDados.get_read_data())
