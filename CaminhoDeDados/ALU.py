from UnidadeDeControle import UnidadeDeControle


class Alu:
    data_1 = None
    data_2 = None
    ALUControl_input: str = None
    ALUOutput = None
    Zero = False

    @classmethod
    def getData_1(cls):
        return cls.data_1

    @classmethod
    def setData_1(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.data_1 = bits.copy()

    @classmethod
    def getData_2(cls):
        return cls.data_2

    @classmethod
    def setData_2(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.data_2 = bits.copy()

    @classmethod
    def setALUControl_input(cls):
        cls.ALUControl_input = UnidadeDeControle.ALUControl.getALUControl_input()

    @classmethod
    def getALUOutput(cls):
        return cls.ALUOutput

    @classmethod
    def zeroActivate(cls):
        return cls.Zero

    @classmethod
    def soma(cls, alu_1: str, alu_2: str):
        vai_um: bool = False
        alu_1 = alu_1[::-1]
        alu_2 = alu_2[::-1]
        for indice, valor in enumerate(alu_2):
            if valor == '0' and alu_1.__getitem__(indice) == '0' and not vai_um:
                aux = list(alu_2)
                aux[indice] = '0'
                alu_2 = "".join(aux)
                vai_um = False
            elif valor == '1' and alu_1.__getitem__(indice) == '0' and not vai_um:
                aux = list(alu_2)
                aux[indice] = '1'
                alu_2 = "".join(aux)
                vai_um = False
            elif valor == '1' and alu_1.__getitem__(indice) == '1' and not vai_um:
                aux = list(alu_2)
                aux[indice] = '0'
                alu_2 = "".join(aux)
                vai_um = True
            elif valor == '0' and alu_1.__getitem__(indice) == '1' and not vai_um:
                aux = list(alu_2)
                aux[indice] = '1'
                alu_2 = "".join(aux)
                vai_um = False
            elif valor == '0' and alu_1.__getitem__(indice) == '0' and vai_um:
                aux = list(alu_2)
                aux[indice] = '1'
                alu_2 = "".join(aux)
                vai_um = False
            elif valor == '1' and alu_1.__getitem__(indice) == '0' and vai_um:
                aux = list(alu_2)
                aux[indice] = '0'
                alu_2 = "".join(aux)
                vai_um = True
            elif valor == '1' and alu_1.__getitem__(indice) == '1' and vai_um:
                aux = list(alu_2)
                aux[indice] = '1'
                alu_2 = "".join(aux)
                vai_um = True
            elif valor == '0' and alu_1.__getitem__(indice) == '1' and vai_um:
                aux = list(alu_2)
                aux[indice] = '0'
                alu_2 = "".join(aux)
                vai_um = True
        return alu_2[::-1]

    @classmethod
    def run(cls):
        alu_1 = ''
        for valor in cls.data_1:
            alu_1 = alu_1 + alu_1.join(valor)

        alu_2 = ''
        for valor in cls.data_2:
            alu_2 = alu_2 + alu_2.join(valor)

        if cls.ALUControl_input.__eq__('0010'):  # soma
            alu_1 = alu_1[::-1]
            alu_2 = alu_2[::-1]
            cls.ALUOutput = Alu.soma(alu_1, alu_2)
            cls.ALUOutput = cls.ALUOutput[::-1]
            aux = []
            for valor in cls.ALUOutput:
                aux.append(valor)
            cls.ALUOutput = aux.copy()
        elif cls.ALUControl_input.__eq__('0110'):  # subtração
            inverter = False
            aux_alu2 = []
            for indice, valor in enumerate(alu_2):
                if valor.__eq__('1') and (not inverter):
                    inverter = True
                elif inverter and valor.__eq__('0'):
                    valor = '1'
                elif inverter and valor.__eq__('1'):
                    valor = '0'
                alu_2[indice] = valor
            alu_2 = ''
            for valor in aux_alu2:
                alu_2 += alu_2.join(valor)
            alu_1 = alu_1[::-1]
            alu_2 = alu_2[::-1]
            cls.ALUOutput = Alu.soma(alu_1, alu_2)
            cls.ALUOutput = cls.ALUOutput[::-1]
            aux = []
            for valor in cls.ALUOutput:
                aux.append(valor)
            cls.ALUOutput = aux.copy()
            cls.Zero = True
            for valor in cls.ALUOutput:
                if valor.__eq__('1'):
                    cls.Zero = False
        elif cls.ALUControl_input.__eq__('0000'):  # and
            aux1 = list(alu_1)
            aux2 = list(alu_2)
            result = []
            for indice in range(32):
                if aux1[indice].__eq__('1') and aux2[indice].__eq__('1'):
                    result[indice] = '1'
                else:
                    result[indice] = '0'
            cls.ALUOutput = result.copy()
        elif cls.ALUControl_input.__eq__('0001'):  # or
            aux1 = list(alu_1)
            aux2 = list(alu_2)
            result = []
            for indice in range(32):
                if aux1[indice].__eq__('1') or aux2[indice].__eq__('1'):
                    result[indice] = '1'
                else:
                    result[indice] = '0'
            cls.ALUOutput = result.copy()
        elif cls.ALUControl_input.__eq__('0111'):  # slt
            soma_1 = 0
            for indice, valor in enumerate(alu_1):
                valor = int(valor) * 2 ** indice
                soma_1 += valor
            soma_2 = 0
            for indice, valor in enumerate(alu_2):
                valor = int(valor) * 2 ** indice
                soma_2 += valor
            if soma_2 > soma_1:
                cls.ALUOutput = list('10000000000000000000000000000000')
            else:
                cls.ALUOutput = list('00000000000000000000000000000000')
        elif cls.ALUControl_input.__eq__('1010'):  # jr
            pass
        elif cls.ALUControl_input.__eq__('1111'):  # sll
            quantidade_deslocamento = alu_2[6:11]
            n = 0
            for indice, valor in enumerate(quantidade_deslocamento):
                valor = int(valor) * 2 ** indice
                n += valor
            for i in range(n):
                cls.data_1.pop()
                cls.data_1.insert(0, '0')
