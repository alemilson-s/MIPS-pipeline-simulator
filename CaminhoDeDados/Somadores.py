class AdderPcMoreFour:
    """
    Somador que faz operação de soma do registrador PC com 4 ‘bytes’
    """
    primeiro_operando = "000000000000000000000000000000000"
    segundo_operando = "000001000000000000000000000000000"  # segundo operando sempre igual a 32 bits -> 4 bytes

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
        return cls.primeiro_operando

    @classmethod
    def run(cls):
        vai_um: bool = False
        for indice, valor in enumerate(cls.primeiro_operando):
            if valor == '0' and cls.segundo_operando.__getitem__(indice) == '0' and not vai_um:
                aux = list(cls.primeiro_operando)
                aux[indice] = '0'
                cls.primeiro_operando = "".join(aux)
                vai_um = False
            elif valor == '1' and cls.segundo_operando.__getitem__(indice) == '0' and not vai_um:
                aux = list(cls.primeiro_operando)
                aux[indice] = '1'
                cls.primeiro_operando = "".join(aux)
                vai_um = False
            elif valor == '1' and cls.segundo_operando.__getitem__(indice) == '1' and not vai_um:
                aux = list(cls.primeiro_operando)
                aux[indice] = '0'
                cls.primeiro_operando = "".join(aux)
                vai_um = True
            elif valor == '0' and cls.segundo_operando.__getitem__(indice) == '1' and not vai_um:
                aux = list(cls.primeiro_operando)
                aux[indice] = '1'
                cls.primeiro_operando = "".join(aux)
                vai_um = False
            elif valor == '0' and cls.segundo_operando.__getitem__(indice) == '0' and vai_um:
                aux = list(cls.primeiro_operando)
                aux[indice] = '1'
                cls.primeiro_operando = "".join(aux)
                vai_um = False
            elif valor == '1' and cls.segundo_operando.__getitem__(indice) == '0' and vai_um:
                aux = list(cls.primeiro_operando)
                aux[indice] = '0'
                cls.primeiro_operando = "".join(aux)
                vai_um = True
            elif valor == '1' and cls.segundo_operando.__getitem__(indice) == '1' and vai_um:
                aux = list(cls.primeiro_operando)
                aux[indice] = '1'
                cls.primeiro_operando = "".join(aux)
                vai_um = True
            elif valor == '0' and cls.segundo_operando.__getitem__(indice) == '1' and vai_um:
                aux = list(cls.primeiro_operando)
                aux[indice] = '0'
                cls.primeiro_operando = "".join(aux)
                vai_um = True
        cls.primeiro_operando = cls.primeiro_operando[::-1]
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
