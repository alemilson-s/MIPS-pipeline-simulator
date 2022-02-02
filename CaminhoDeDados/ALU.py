from CaminhoDeDados.Pipeline import Registradores
from UnidadeDeControle import UnidadeDeControle


class Alu:
    data_1 = None  # primeiro operando da ALU
    data_2 = None  # segundo operando da ALU
    ALUControl_output: str = None  # bits que indicam a operação a ser feita na ALU
    ALUOutput = None  # saída da ALU
    Zero = False  # indica se o resultado da operação da ALU foi zero

    @classmethod
    def get_data_1(cls):
        return cls.data_1

    @classmethod
    def set_data_1(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.data_1 = bits.copy()

    @classmethod
    def get_data_2(cls):
        return cls.data_2

    @classmethod
    def set_data_2(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.data_2 = bits.copy()

    @classmethod
    def set_alu_control_output(cls):
        """
        Atualiza os 4 bits que indicam a operação a ser feita na ALU
        Sem retorno
        """
        cls.ALUControl_output = UnidadeDeControle.ALUControl.get_alu_control_output()

    @classmethod
    def get_alu_output(cls):
        return cls.ALUOutput

    @classmethod
    def zero_is_activate(cls):
        """
        Retorna se o resultado da operação feita ALU é igual a zero
        Atributo Zero da ALU
        """
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
        alu_1 = ''  # Guarda conversão do primeiro operando da ALU em uma 'string'
        for valor in cls.data_1:
            alu_1 = alu_1 + alu_1.join(valor)

        alu_2 = ''  # Guarda conversão do segundo operando da ALU em uma ‘string’
        for valor in cls.data_2:
            alu_2 = alu_2 + alu_2.join(valor)

        if cls.ALUControl_output.__eq__('0010'):  # soma
            alu_1 = alu_1[::-1]  # inversão feita para facilitar soma
            alu_2 = alu_2[::-1]  # inversão feita para facilitar soma
            cls.ALUOutput = Alu.soma(alu_1, alu_2)  # guardando resultado da soma em formato 'string'
            cls.ALUOutput = cls.ALUOutput[::-1]  # inversão para voltar ao normal
            cls.ALUOutput = list(cls.ALUOutput)  # convertendo em lista
        elif cls.ALUControl_output.__eq__('0110'):  # subtração
            inverter = False
            aux_alu2 = []
            # tornando segundo operando da ALU negativo — inicio
            for indice, valor in enumerate(alu_2):
                if valor.__eq__('1') and (not inverter):
                    inverter = True
                elif inverter and valor.__eq__('0'):
                    valor = '1'
                elif inverter and valor.__eq__('1'):
                    valor = '0'
                aux_alu2.insert(indice, valor)
            alu_2 = ''
            for valor in aux_alu2:
                alu_2 += alu_2.join(valor)
            # tornando segundo operando da ALU negativo — fim
            alu_1 = alu_1[::-1]
            alu_2 = alu_2[::-1]
            cls.ALUOutput = Alu.soma(alu_1, alu_2)
            cls.ALUOutput = cls.ALUOutput[::-1]
            cls.ALUOutput = list(cls.ALUOutput)
            cls.Zero = True
            for valor in cls.ALUOutput:
                if valor.__eq__('1'):
                    cls.Zero = False
        elif cls.ALUControl_output.__eq__('0000'):  # and
            aux1 = list(alu_1)
            aux2 = list(alu_2)
            result = []
            for indice in range(32):
                if aux1[indice].__eq__('1') and aux2[indice].__eq__('1'):
                    result.insert(indice, '1')
                else:
                    result.insert(indice, '0')
            cls.ALUOutput = result.copy()
        elif cls.ALUControl_output.__eq__('0001'):  # or
            aux1 = list(alu_1)
            aux2 = list(alu_2)
            result = []
            for indice in range(32):
                if aux1[indice].__eq__('1') or aux2[indice].__eq__('1'):
                    result.insert(indice, '1')
                else:
                    result.insert(indice, '0')
            cls.ALUOutput = result.copy()
        elif cls.ALUControl_output.__eq__('0111'):  # slt
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
        elif cls.ALUControl_output.__eq__('1010'):  # jr
            pass
        elif cls.ALUControl_output.__eq__('1111'):  # sll
            aux = Registradores.IDEX.get_instruction_0_15()
            quantidade_deslocamento = aux[6:11]
            n = 0
            for indice, valor in enumerate(quantidade_deslocamento):
                valor = int(valor) * (2 ** indice)
                n += valor
            for i in range(n):
                cls.data_2.pop()
                cls.data_2.insert(0, '0')
            cls.ALUOutput = cls.data_2.copy()
