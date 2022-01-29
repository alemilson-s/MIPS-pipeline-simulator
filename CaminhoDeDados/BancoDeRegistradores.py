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
    RegWrite = False

    @classmethod
    def set_reg_write(cls, sinal):
        cls.RegWrite = sinal

    @classmethod
    def run(cls):
        if cls.RegWrite:
            cls.write()

    @classmethod
    def set_read_register_1(cls, numero_registrador):
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
    def set_read_register_2(cls, numero_registrador):
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
    def set_write_register(cls, numero_registrador):
        if len(numero_registrador) == 5:
            if type(numero_registrador) == list:
                cls.writeRegister = ""
                for valor in numero_registrador:
                    cls.writeRegister = cls.writeRegister + "".join(valor)
                cls.writeRegister = cls.writeRegister[::-1]
            else:
                cls.writeRegister = numero_registrador

    @classmethod
    def set_write_data(cls, bits):
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
        if cls.writeRegister == V0.get_id():
            V0.set(cls.writeData)
        elif cls.writeRegister == V1.get_id():
            V1.set(cls.writeData)
        elif cls.writeRegister == A0.get_id():
            A0.set(cls.writeData)
        elif cls.writeRegister == A1.get_id():
            A1.set(cls.writeData)
        elif cls.writeRegister == A2.get_id():
            A2.set(cls.writeData)
        elif cls.writeRegister == A3.get_id():
            A3.set(cls.writeData)
        elif cls.writeRegister == T0.get_id():
            T0.set(cls.writeData)
        elif cls.writeRegister == T1.get_id():
            T1.set(cls.writeData)
        elif cls.writeRegister == T2.get_id():
            T2.set(cls.writeData)
        elif cls.writeRegister == T3.get_id():
            T3.set(cls.writeData)
        elif cls.writeRegister == T4.get_id():
            T4.set(cls.writeData)
        elif cls.writeRegister == T5.get_id():
            T5.set(cls.writeData)
        elif cls.writeRegister == T6.get_id():
            T6.set(cls.writeData)
        elif cls.writeRegister == T7.get_id():
            T7.set(cls.writeData)
        elif cls.writeRegister == S0.get_id():
            S0.set(cls.writeData)
        elif cls.writeRegister == S1.get_id():
            S1.set(cls.writeData)
        elif cls.writeRegister == S2.get_id():
            S2.set(cls.writeData)
        elif cls.writeRegister == S3.get_id():
            S3.set(cls.writeData)
        elif cls.writeRegister == S4.get_id():
            S4.set(cls.writeData)
        elif cls.writeRegister == S5.get_id():
            S5.set(cls.writeData)
        elif cls.writeRegister == S6.get_id():
            S6.set(cls.writeData)
        elif cls.writeRegister == S7.get_id():
            S7.set(cls.writeData)
        elif cls.writeRegister == T8.get_id():
            T8.set(cls.writeData)
        elif cls.writeRegister == T9.get_id():
            T9.set(cls.writeData)
        elif cls.writeRegister == Sp.get_id():
            Sp.set(cls.writeData)
        elif cls.writeRegister == Ra.get_id():
            Ra.set(cls.writeData)
        else:
            print("Registrador não encontrado!")

    @classmethod
    def get_read_data_1(cls):
        if cls.readRegister1 == Zero.get_id():
            return Zero.bits
        elif cls.readRegister1 == V0.get_id():
            return V0.get()
        elif cls.readRegister1 == V1.get_id():
            return V1.get()
        elif cls.readRegister1 == A0.get_id():
            return A0.get()
        elif cls.readRegister1 == A1.get_id():
            return A1.get()
        elif cls.readRegister1 == A2.get_id():
            return A2.get()
        elif cls.readRegister1 == A3.get_id():
            return A3.get()
        elif cls.readRegister1 == T0.get_id():
            return T0.get()
        elif cls.readRegister1 == T1.get_id():
            return T1.get()
        elif cls.readRegister1 == T2.get_id():
            return T2.get()
        elif cls.readRegister1 == T3.get_id():
            return T3.get()
        elif cls.readRegister1 == T4.get_id():
            return T4.get()
        elif cls.readRegister1 == T5.get_id():
            return T5.get()
        elif cls.readRegister1 == T6.get_id():
            return T6.get()
        elif cls.readRegister1 == T7.get_id():
            return T7.get()
        elif cls.readRegister1 == S0.get_id():
            return S0.get()
        elif cls.readRegister1 == S1.get_id():
            return S1.get()
        elif cls.readRegister1 == S2.get_id():
            return S2.get()
        elif cls.readRegister1 == S3.get_id():
            return S3.get()
        elif cls.readRegister1 == S4.get_id():
            return S4.get()
        elif cls.readRegister1 == S5.get_id():
            return S5.get()
        elif cls.readRegister1 == S6.get_id():
            return S6.get()
        elif cls.readRegister1 == S7.get_id():
            return S7.get()
        elif cls.readRegister1 == T8.get_id():
            return T8.get()
        elif cls.readRegister1 == T9.get_id():
            return T9.get()
        elif cls.readRegister1 == Sp.get_id():
            return Sp.get()
        elif cls.readRegister1 == Ra.get_id():
            return Ra.get()
        else:
            print("Registrador não encontrado!")

    @classmethod
    def get_read_data_2(cls):
        if cls.readRegister2 == Zero.get_id():
            return Zero.bits
        elif cls.readRegister2 == V0.get_id():
            return V0.get()
        elif cls.readRegister2 == V1.get_id():
            return V1.get()
        elif cls.readRegister2 == A0.get_id():
            return A0.get()
        elif cls.readRegister2 == A1.get_id():
            return A1.get()
        elif cls.readRegister2 == A2.get_id():
            return A2.get()
        elif cls.readRegister2 == A3.get_id():
            return A3.get()
        elif cls.readRegister2 == T0.get_id():
            return T0.get()
        elif cls.readRegister2 == T1.get_id():
            return T1.get()
        elif cls.readRegister2 == T2.get_id():
            return T2.get()
        elif cls.readRegister2 == T3.get_id():
            return T3.get()
        elif cls.readRegister2 == T4.get_id():
            return T4.get()
        elif cls.readRegister2 == T5.get_id():
            return T5.get()
        elif cls.readRegister2 == T6.get_id():
            return T6.get()
        elif cls.readRegister2 == T7.get_id():
            return T7.get()
        elif cls.readRegister2 == S0.get_id():
            return S0.get()
        elif cls.readRegister2 == S1.get_id():
            return S1.get()
        elif cls.readRegister2 == S2.get_id():
            return S2.get()
        elif cls.readRegister2 == S3.get_id():
            return S3.get()
        elif cls.readRegister2 == S4.get_id():
            return S4.get()
        elif cls.readRegister2 == S5.get_id():
            return S5.get()
        elif cls.readRegister2 == S6.get_id():
            return S6.get()
        elif cls.readRegister2 == S7.get_id():
            return S7.get()
        elif cls.readRegister2 == T8.get_id():
            return T8.get()
        elif cls.readRegister2 == T9.get_id():
            return T9.get()
        elif cls.readRegister2 == Sp.get_id():
            return Sp.get()
        elif cls.readRegister2 == Ra.get_id():
            return Ra.get()
        else:
            print("Registrador não encontrado!")


class Zero:
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
        ‘id’ → número do registrador
        """
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class V0:
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
        Método para alterar os valores do intervalo fechado de bit inicial a bit final
        bit inicial: Representa a posição inicial do bit ao qual iremos percorrer
        bit final: Representa a posição final do bit ao qual iremos percorrer
        sequencia de bits: Valores ao qual serão inseridos na lista de bits
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
        Método para retornar os valores do intervalo fechado de bit inicial a bit final
        bit inicial: Representa a posição inicial do bit ao qual iremos percorrer
        bit final: Representa a posição final do bit ao qual iremos percorrer
        bits contidos no intervalo fechado → [bit inicial, bit final]
        """
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits[bit_inicial:(bit_final + 1)]

    @classmethod
    def set(cls, bits):
        """
        Método para alterar os 32 bits da lista(bits) representando os bits do registrador
        bits: String ou lista representando 32 bits
        Não há retorno
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
        Método para retornar os 32 bits contidos no registrador
        'bits'(lista que representa os 32 bits do registrador)
        """
        if not cls.inicializado:
            cls.inicializar()

        return cls.bits

    @classmethod
    def get_id(cls):
        """
        Retorna o campo 'id' do registrador
        ‘id’ → número do registrador
        """
        if not cls.inicializado:
            cls.inicializar()

        return cls.id


class V1:
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


class A0:
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


class A1:
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


class A2:
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


class A3:
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


class T0:
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


class T1:
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


class T2:
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


class T3:
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


class T4:
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


class T5:
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


class T6:
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


class T7:
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


class S0:
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


class S1:
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


class S2:
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


class S3:
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


class S4:
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


class S5:
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


class S6:
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


class S7:
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


class T8:
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


class T9:
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


class Sp:
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


class Ra:
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

# BancoDeRegistradores.setReadRegister1(list("01000"))
# BancoDeRegistradores.setWriteRegister("00010")
# BancoDeRegistradores.setWriteData("11110000100000000000000000000000")
# BancoDeRegistradores.write()
# print(v0.get())
