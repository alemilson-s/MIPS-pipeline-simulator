class BancoDeRegistradores:
    """
    Classe representando o bancdo de registradores
    """
    readRegister1 = None  # Número do registrador operando 1 do bando de registradores
    readRegister2 = None  # Número do registrador operando 2 do bonco de registradores
    writeRegister = None  # Número do Registrador a ser escrito
    writeData = None  # Bits do dado a ser escrito
    readData1 = None  # Bits do dado contido no primeiro operando
    readData2 = None  # Bits do dado contido no segundo operando

    @classmethod
    def setReadRegister1(cls, numero_registrador):
        if len(numero_registrador) == 5:
            if type(numero_registrador) == list:
                cls.readRegister1 = ""
                for valor in numero_registrador:
                    cls.readRegister1 = cls.readRegister1 + "".join(valor)
                cls.readRegister1 = cls.readRegister1[::-1]
            else:
                cls.readRegister1 = numero_registrador
        else:
            print("Número de bits deve ser igual à 5!")

    @classmethod
    def setReadRegister2(cls, numero_registrador):
        if len(numero_registrador) == 5:
            if type(numero_registrador) == list:
                cls.readRegister2 = ""
                for valor in numero_registrador:
                    cls.readRegister2 = cls.readRegister2 + "".join(valor)
                cls.readRegister2 = cls.readRegister2[::-1]
            else:
                cls.readRegister2 = numero_registrador
        else:
            print("Número de bits deve ser igual à 5!")

    @classmethod
    def setWriteRegister(cls, numero_registrador):
        if len(numero_registrador) == 5:
            if type(numero_registrador) == list:
                cls.writeRegister = ""
                for valor in numero_registrador:
                    cls.writeRegister = cls.writeRegister + "".join(valor)
                cls.writeRegister = cls.writeRegister[::-1]
            else:
                cls.writeRegister = numero_registrador

    @classmethod
    def setWriteData(cls, bits):
        if len(bits) == 32:
            if type(bits) == list:
                cls.writeData = bits
            else:
                cls.writeData = []
                for valor in bits:
                    cls.writeData.insert(0, valor)

    @classmethod
    def write(cls):
        """
        Método para escrever no banco de registradores
        :return:
        """
        if cls.writeRegister == v0.get_id():
            v0.set(cls.writeData)
        elif cls.writeRegister == v1.get_id():
            v1.set(cls.writeData)
        elif cls.writeRegister == a0.get_id():
            a0.set(cls.writeData)
        elif cls.writeRegister == a1.get_id():
            a1.set(cls.writeData)
        elif cls.writeRegister == a2.get_id():
            a2.set(cls.writeData)
        elif cls.writeRegister == a3.get_id():
            a3.set(cls.writeData)
        elif cls.writeRegister == t0.get_id():
            t0.set(cls.writeData)
        elif cls.writeRegister == t1.get_id():
            t1.set(cls.writeData)
        elif cls.writeRegister == t2.get_id():
            t2.set(cls.writeData)
        elif cls.writeRegister == t3.get_id():
            t3.set(cls.writeData)
        elif cls.writeRegister == t4.get_id():
            t4.set(cls.writeData)
        elif cls.writeRegister == t5.get_id():
            t5.set(cls.writeData)
        elif cls.writeRegister == t6.get_id():
            t6.set(cls.writeData)
        elif cls.writeRegister == t7.get_id():
            t7.set(cls.writeData)
        elif cls.writeRegister == s0.get_id():
            s0.set(cls.writeData)
        elif cls.writeRegister == s1.get_id():
            s1.set(cls.writeData)
        elif cls.writeRegister == s2.get_id():
            s2.set(cls.writeData)
        elif cls.writeRegister == s3.get_id():
            s3.set(cls.writeData)
        elif cls.writeRegister == s4.get_id():
            s4.set(cls.writeData)
        elif cls.writeRegister == s5.get_id():
            s5.set(cls.writeData)
        elif cls.writeRegister == s6.get_id():
            s6.set(cls.writeData)
        elif cls.writeRegister == s7.get_id():
            s7.set(cls.writeData)
        elif cls.writeRegister == t8.get_id():
            t8.set(cls.writeData)
        elif cls.writeRegister == t9.get_id():
            t9.set(cls.writeData)
        elif cls.writeRegister == sp.get_id():
            sp.set(cls.writeData)
        elif cls.writeRegister == ra.get_id():
            ra.set(cls.writeData)
        else:
            print("Registrador não encontrado!")

    @classmethod
    def getReadData1(cls):
        if cls.readRegister1 == zero.get_id():
            return zero.bits
        elif cls.readRegister1 == v0.get_id():
            return v0.get()
        elif cls.readRegister1 == v1.get_id():
            return v1.get()
        elif cls.readRegister1 == a0.get_id():
            return a0.get()
        elif cls.readRegister1 == a1.get_id():
            return a1.get()
        elif cls.readRegister1 == a2.get_id():
            return a2.get()
        elif cls.readRegister1 == a3.get_id():
            return a3.get()
        elif cls.readRegister1 == t0.get_id():
            return t0.get()
        elif cls.readRegister1 == t1.get_id():
            return t1.get()
        elif cls.readRegister1 == t2.get_id():
            return t2.get()
        elif cls.readRegister1 == t3.get_id():
            return t3.get()
        elif cls.readRegister1 == t4.get_id():
            return t4.get()
        elif cls.readRegister1 == t5.get_id():
            return t5.get()
        elif cls.readRegister1 == t6.get_id():
            return t6.get()
        elif cls.readRegister1 == t7.get_id():
            return t7.get()
        elif cls.readRegister1 == s0.get_id():
            return s0.get()
        elif cls.readRegister1 == s1.get_id():
            return s1.get()
        elif cls.readRegister1 == s2.get_id():
            return s2.get()
        elif cls.readRegister1 == s3.get_id():
            return s3.get()
        elif cls.readRegister1 == s4.get_id():
            return s4.get()
        elif cls.readRegister1 == s5.get_id():
            return s5.get()
        elif cls.readRegister1 == s6.get_id():
            return s6.get()
        elif cls.readRegister1 == s7.get_id():
            return s7.get()
        elif cls.readRegister1 == t8.get_id():
            return t8.get()
        elif cls.readRegister1 == t9.get_id():
            return t9.get()
        elif cls.readRegister1 == sp.get_id():
            return sp.get()
        elif cls.readRegister1 == ra.get_id():
            return ra.get()
        else:
            print("Registrador não encontrado!")

    @classmethod
    def getReadData2(cls):
        if cls.readRegister2 == zero.get_id():
            return zero.bits
        elif cls.readRegister2 == v0.get_id():
            return v0.get()
        elif cls.readRegister2 == v1.get_id():
            return v1.get()
        elif cls.readRegister2 == a0.get_id():
            return a0.get()
        elif cls.readRegister2 == a1.get_id():
            return a1.get()
        elif cls.readRegister2 == a2.get_id():
            return a2.get()
        elif cls.readRegister2 == a3.get_id():
            return a3.get()
        elif cls.readRegister2 == t0.get_id():
            return t0.get()
        elif cls.readRegister2 == t1.get_id():
            return t1.get()
        elif cls.readRegister2 == t2.get_id():
            return t2.get()
        elif cls.readRegister2 == t3.get_id():
            return t3.get()
        elif cls.readRegister2 == t4.get_id():
            return t4.get()
        elif cls.readRegister2 == t5.get_id():
            return t5.get()
        elif cls.readRegister2 == t6.get_id():
            return t6.get()
        elif cls.readRegister2 == t7.get_id():
            return t7.get()
        elif cls.readRegister2 == s0.get_id():
            return s0.get()
        elif cls.readRegister2 == s1.get_id():
            return s1.get()
        elif cls.readRegister2 == s2.get_id():
            return s2.get()
        elif cls.readRegister2 == s3.get_id():
            return s3.get()
        elif cls.readRegister2 == s4.get_id():
            return s4.get()
        elif cls.readRegister2 == s5.get_id():
            return s5.get()
        elif cls.readRegister2 == s6.get_id():
            return s6.get()
        elif cls.readRegister2 == s7.get_id():
            return s7.get()
        elif cls.readRegister2 == t8.get_id():
            return t8.get()
        elif cls.readRegister2 == t9.get_id():
            return t9.get()
        elif cls.readRegister2 == sp.get_id():
            return sp.get()
        elif cls.readRegister2 == ra.get_id():
            return ra.get()
        else:
            print("Registrador não encontrado!")


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
    id = '00010'
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
    id = '00011'
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
    id = '00100'
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
    id = '00101'
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
    id = '00110'
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
    id = '00111'
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
    id = '01000'
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
    id = '01001'
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
    id = '01010'
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
    id = '01011'
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
    id = '01100'
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
    id = '01101'
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
    id = '01110'
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
    id = '01111'
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
    id = '10000'
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
    id = '10001'
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
    id = '10010'
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
    id = '10011'
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
    id = '10100'
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
    id = '10101'
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
    id = '10110'
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
    id = '10111'
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
    id = '11000'
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
    id = '11001'
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
    id = '11101'
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
    id = '11111'
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


BancoDeRegistradores.setReadRegister1(list("01000"))
BancoDeRegistradores.setWriteRegister("00010")
BancoDeRegistradores.setWriteData("11110000100000000000000000000000")
BancoDeRegistradores.write()
print(v0.get())
