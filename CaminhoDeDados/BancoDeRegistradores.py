class zero:
    """
    Classe representando o registrador $zero
    """

    bits: list = []  # Lista utilizada para representar os 32 bits do registrador $zero
    id = '00000'

    @classmethod
    def inicializar(cls):
        """
        Método para colocar todos os bits do registrador $zero com o valor '0'
        :return: O método não possui retorno
        """
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def get_id(cls):
        """
        Retorna o campo 'id' do registrador
        :return: id -> número do registrador
        """
        return cls.id


class v0:
    """
    Classe representando o registrador $zero
    """
    bits: list = []  # Lista utilizada para representar os 32 bits do registrador
    id = '000010'

    @classmethod
    def inicializar(cls):
        """
        Método para colocar todos os bits do registrador $v0 com o valor '0'
        :return: O método não possui retorno
        """
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        """
        Método para alterar os valores do intervalo fechado de bit_inicial a bit_final
        :param bit_inicial: Representa a posição inicial do bit ao qual iremos percorrer
        :param bit_final: Representa a posição final do bit ao qual iremos percorrer
        :param sequencia_de_bits: Valores ao qual serão inseridos na lista de bits
        :return: Função sem retorno
        """

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)

        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        """
        Método para retornar os valores do intervalo fechado de bit_inicial a bit_final
        :param bit_inicial: Representa a posição inicial do bit ao qual iremos percorrer
        :param bit_final: Representa a posição final do bit ao qual iremos percorrer
        :return: bits contido no intervalo fechado -> [bit_inicial, bit_final]
        """
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        """
        Método para alterar os 32 bits da lista(bits) representando os bits do registrador
        :param bits: String ou lista representando 32 bits
        :return: Não há retorno
        """
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        """
        Método para retornar os 32 bits contido no registrador
        :return: bits(lista que representa os 32 bits do registrador)
        """
        return cls.bits

    @classmethod
    def get_id(cls):
        """
        Retorna o campo 'id' do registrador
        :return: id -> número do registrador
        """
        return cls.id


class v1:
    bits: list = []
    id = '000011'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class a0:
    bits: list = []
    id = '000100'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class a1:
    bits: list = []
    id = '000101'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class a2:
    bits: list = []
    id = '000110'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class a3:
    bits: list = []
    id = '000111'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t0:
    bits: list = []
    id = '001000'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t1:
    bits: list = []
    id = '001001'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t2:
    bits: list = []
    id = '001010'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t3:
    bits: list = []
    id = '001011'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t4:
    bits: list = []
    id = '001100'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t5:
    bits: list = []
    id = '001101'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t6:
    bits: list = []
    id = '001110'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t7:
    bits: list = []
    id = '001111'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class s0:
    bits: list = []
    id = '010000'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class s1:
    bits: list = []
    id = '010001'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class s2:
    bits: list = []
    id = '010010'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class s3:
    bits: list = []
    id = '010011'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class s4:
    bits: list = []
    id = '010100'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class s5:
    bits: list = []
    id = '010101'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class s6:
    bits: list = []
    id = '010110'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class s7:
    bits: list = []
    id = '010111'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t8:
    bits: list = []
    id = '011000'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class t9:
    bits: list = []
    id = '011001'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class sp:
    bits: list = []
    id = '011101'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id


class ra:
    bits: list = []
    id = '011111'

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.bits = bits.copy()
        elif len(bits) == 32:
            cls.bits.clear()
            for valor in bits:
                cls.bits.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def get_id(cls):
        return cls.id
