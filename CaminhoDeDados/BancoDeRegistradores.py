class zero:
    """
    Classe representando o registrador $zero
    """

    bits: list = []  # Lista utilizada para representar os 32 bits do registrador $zero
    id = '00000'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        """
        Método para colocar todos os bits do registrador $zero com o valor '0'
        :return: O método não possui retorno
        """
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def get_id(cls):
        """
        Retorna o campo 'id' do registrador
        :return: id -> número do registrador
        """
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class v0:
    """
    Classe representando o registrador $zero
    """
    bits: list = []  # Lista utilizada para representar os 32 bits do registrador
    id = '000010'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        """
        Método para colocar todos os bits do registrador $v0 com o valor '0'
        :return: O método não possui retorno
        """
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        """
        Método para alterar os valores do intervalo fechado de bit_inicial a bit_final
        :param bit_inicial: Representa a posição inicial do bit ao qual iremos percorrer
        :param bit_final: Representa a posição final do bit ao qual iremos percorrer
        :param sequencia_de_bits: Valores ao qual serão inseridos na lista de bits
        :return: Função sem retorno
        """
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        """
        Método para alterar os 32 bits da lista(bits) representando os bits do registrador
        :param bits: String ou lista representando 32 bits
        :return: Não há retorno
        """
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        """
        Retorna o campo 'id' do registrador
        :return: id -> número do registrador
        """
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class v1:
    bits: list = []
    id = '000011'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class a0:
    bits: list = []
    id = '000100'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class a1:
    bits: list = []
    id = '000101'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class a2:
    bits: list = []
    id = '000110'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class a3:
    bits: list = []
    id = '000111'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t0:
    bits: list = []
    id = '001000'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t1:
    bits: list = []
    id = '001001'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t2:
    bits: list = []
    id = '001010'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t3:
    bits: list = []
    id = '001011'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()
        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t4:
    bits: list = []
    id = '001100'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t5:
    bits: list = []
    id = '001101'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t6:
    bits: list = []
    id = '001110'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t7:
    bits: list = []
    id = '001111'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class s0:
    bits: list = []
    id = '010000'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class s1:
    bits: list = []
    id = '010001'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class s2:
    bits: list = []
    id = '010010'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class s3:
    bits: list = []
    id = '010011'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class s4:
    bits: list = []
    id = '010100'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class s5:
    bits: list = []
    id = '010101'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class s6:
    bits: list = []
    id = '010110'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class s7:
    bits: list = []
    id = '010111'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t8:
    bits: list = []
    id = '011000'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class t9:
    bits: list = []
    id = '011001'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class sp:
    bits: list = []
    id = '011101'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class ra:
    bits: list = []
    id = '011111'
    inicializado: bool = False

    @classmethod
    def inicializar(cls):
        for contador in range(32):
            cls.bits.insert(0, '0')
        cls.inicializado = True

    @classmethod
    def set_bits(cls, bit_inicial, bit_final, sequencia_de_bits):
        if not cls.inicializado:
            cls.inicializar()

        if type(sequencia_de_bits) != list:
            sequencia_de_bits = list(sequencia_de_bits)
        cont: int = 0
        for valor in range(bit_inicial, bit_final + 1):
            cls.bits[valor] = sequencia_de_bits[cont]
            cont += 1

    @classmethod
    def get_bits(cls, bit_inicial, bit_final):
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        if not cls.inicializado:
            cls.inicializar()

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
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        if not cls.inicializado:
            cls.inicializar()

        return cls.id
