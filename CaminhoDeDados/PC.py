class PC:
    bits: list = list("00000000000000000000000000000000")  # lista representando os 32 bits do registrador PC

    @classmethod
    def set_pc(cls, bits):
        if type(bits) is list and len(bits) == 32:
            cls.bits = bits.copy()

    @classmethod
    def get_pc(cls):
        return cls.bits
