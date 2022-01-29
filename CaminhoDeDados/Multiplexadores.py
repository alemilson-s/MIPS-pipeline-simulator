class MuxPC:
    bits_0: list = list("00000000000000000000000000000000")  # somador PC + 4
    bits_1: list = list("00000000000000000000000000000000")  # desvio condicional
    sinal_de_controle: bool = False

    @classmethod
    def set_sinal_de_controle(cls, sinal):
        cls.sinal_de_controle = sinal

    @classmethod
    def set_bits_0(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_0 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def set_bits_1(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_1 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def get(cls):
        if cls.sinal_de_controle is True:
            return cls.bits_1
        elif cls.sinal_de_controle is False:
            return cls.bits_0


class MuxAlu1:
    bits_0 = list("00000000000000000000000000000000")  # banco de registradores
    bits_1 = list("00000000000000000000000000000000")  # memoria de dadou ou alu
    bits_2 = list("00000000000000000000000000000000")  # alu
    sinal_de_controle: str = '00'

    @classmethod
    def set_sinal_de_controle(cls, sinal):
        if type(sinal) is str and len(sinal) == 2:
            cls.sinal_de_controle = sinal
        else:
            print("Espera-se receber como parâmetro uma string de 2 bits!")

    @classmethod
    def set_bits_0(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_0 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def set_bits_1(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_1 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def set_bits_2(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_2 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def get(cls):
        if cls.sinal_de_controle.__eq__("00"):
            return cls.bits_0
        elif cls.sinal_de_controle.__eq__("01"):
            return cls.bits_1
        elif cls.sinal_de_controle.__eq__("10"):
            return cls.bits_2


class MuxAlu2:
    bits_0 = list("00000000000000000000000000000000")  # banco de registradores
    bits_1 = list("00000000000000000000000000000000")  # memoria de dadou ou alu
    bits_2 = list("00000000000000000000000000000000")  # alu
    sinal_de_controle: str = '00'

    @classmethod
    def set_sinal_de_controle(cls, sinal):
        if type(sinal) is str and len(sinal) == 2:
            cls.sinal_de_controle = sinal
        else:
            print("Espera-se receber como parâmetro uma string de 2 bits!")

    @classmethod
    def set_bits_0(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_0 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def set_bits_1(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_1 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def set_bits_2(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_2 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def get(cls):
        if cls.sinal_de_controle.__eq__("00"):
            return cls.bits_0
        elif cls.sinal_de_controle.__eq__("01"):
            return cls.bits_1
        elif cls.sinal_de_controle.__eq__("10"):
            return cls.bits_2


class MuxEXMEM:
    bits_0: list = list("00000")  # bits [16-20] da instrução
    bits_1: list = list("00000")  # bits [11-15] da instrução
    sinal_de_controle: bool = False

    @classmethod
    def set_sinal_de_controle(cls, sinal):
        cls.sinal_de_controle = sinal

    @classmethod
    def set_bits_0(cls, bits):
        if type(bits) is list and len(bits) == 5:
            cls.bits_0 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 5 bits!")

    @classmethod
    def set_bits_1(cls, bits):
        if type(bits) is list and len(bits) == 5:
            cls.bits_1 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 5 bits!")

    @classmethod
    def get(cls):
        if cls.sinal_de_controle is True:
            return cls.bits_1
        elif cls.sinal_de_controle is False:
            return cls.bits_0


class MuxReg:
    bits_0: list = list("00000000000000000000000000000000")  # conteúdo lido da memória
    bits_1: list = list("00000000000000000000000000000000")  # saída da ALU
    sinal_de_controle: bool = False

    @classmethod
    def set_sinal_de_controle(cls, sinal):
        cls.sinal_de_controle = sinal

    @classmethod
    def set_bits_0(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_0 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def set_bits_1(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits_1 = bits.copy()
        else:
            print("Espera-se receber como parâmetro uma lista de 32 bits!")

    @classmethod
    def get(cls):
        if cls.sinal_de_controle is True:
            return cls.bits_1
        elif cls.sinal_de_controle is False:
            return cls.bits_0
