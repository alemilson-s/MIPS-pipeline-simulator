def soma(alu_1: str, alu_2: str):
    """
    Recebe os dois parametros como ‘strings’ no formato com o bit zero sendo o bit mais a esquerda
    """
    vai_um: bool = False
    # alu_1 = alu_1[::-1]
    # alu_2 = alu_2[::-1]
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


class PrimeiroSomador:
    """
    Somador que faz operação de soma do registrador PC com 4 ‘bytes’
    """
    primeiro_operando = "00000000000000000000000000000000"
    segundo_operando = "00000100000000000000000000000000"  # segundo operando sempre igual a 32 bits -> 4 bytes
    output = "00000000000000000000000000000000"

    @classmethod
    def set_primeiro_operando(cls, bits):
        """
        Como PC retorna uma ‘string’ representando o endereço com o bit na posição zero sendo o bit mais à direita,
        fazemos a operação de inversão da ‘string’ para realização da soma
        """
        if type(bits) is str:
            cls.primeiro_operando = bits[::-1]
        else:
            print("Espera-se receber como parâmetro uma string!")

    @classmethod
    def get(cls):
        """
        Retorna 32 bits com o bit da posição zero sendo o bit mais a direita
        """
        return list(cls.output[::-1])

    @classmethod
    def run(cls):
        cls.output = soma(cls.primeiro_operando, cls.segundo_operando)


class SegundoSomador:
    primeiro_operando = "00000000000000000000000000000000"
    segundo_operando = "00000000000000000000000000000000"
    output = "00000000000000000000000000000000"

    @classmethod
    def set_primeiro_operando(cls, bits):
        if type(bits) is list:
            cls.primeiro_operando = ''
            for bit in bits:
                cls.primeiro_operando = cls.primeiro_operando + cls.primeiro_operando.join(bit)
        else:
            print("Espera-se receber como parâmetro uma lista!")

    @classmethod
    def set_segundo_operando(cls, bits):
        if type(bits) is list:
            cls.segundo_operando = ''
            for bit in bits:
                cls.segundo_operando = cls.segundo_operando + cls.segundo_operando.join(bit)
        else:
            print("Espera-se receber como parâmetro uma lista!")

    @classmethod
    def get(cls):
        """
        Retorna uma lista com 32 bits contendo o resultado da soma de operando1 com operando 2
        """
        return list(cls.output[::-1])

    @classmethod
    def run(cls):
        cls.output = soma(cls.primeiro_operando, cls.segundo_operando)

# Exemplos de utilização
# AdderPCMoreFour.set_primeiro_operando(PC.get_pc())
# AdderPCMoreFour.run()
# PC.set_pc(AdderPCMoreFour.get())
# print(PC.get_pc())
# AdderPCMoreFour.set_primeiro_operando(PC.get_pc())
# AdderPCMoreFour.run()
# PC.set_pc(AdderPCMoreFour.get())
# print(PC.get_pc())
# AdderPCMoreFour.set_primeiro_operando(PC.get_pc())
# AdderPCMoreFour.run()
# PC.set_pc(AdderPCMoreFour.get())
# print(PC.get_pc())
# AdderPCMoreFour.set_primeiro_operando(PC.get_pc())
# AdderPCMoreFour.run()
# PC.set_pc(AdderPCMoreFour.get())
# print(PC.get_pc())
# AdderPCMoreFour.set_primeiro_operando(PC.get_pc())
# AdderPCMoreFour.run()
# PC.set_pc(AdderPCMoreFour.get())
# print(PC.get_pc())
# AdderPCMoreFour.set_primeiro_operando(PC.get_pc())
# AdderPCMoreFour.run()
# PC.set_pc(AdderPCMoreFour.get())
# print(PC.get_pc())
# SegundoSomador.set_primeiro_operando(list("00010000000000000000000000000000"))
# SegundoSomador.set_segundo_operando(list("10100000000000000000000000000000"))
# SegundoSomador.run()
# print(SegundoSomador.get())
