class Pc:
    bits: list = list("00000000000000000000000000000000")  # lista representando os 32 bits do registrador PC

    @classmethod
    def set_pc(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits = bits.copy()
        elif type(bits) is str and len(bits) == 32:
            bits = bits[::-1]
            cls.bits = list(bits)

    @classmethod
    def get_pc(cls):
        """
        Retorna o endereço contido em PC com o bit zero sendo o bit mais a direita
        """
        endereco: str = ''
        for indice, valor in enumerate(cls.bits):
            endereco += cls.bits[indice]
        return endereco[::-1]
