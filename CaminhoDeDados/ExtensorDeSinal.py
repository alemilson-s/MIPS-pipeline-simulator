class ExtensorDeSinal:
    bits = list("0000000000000000")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def set_bits(cls, bits):
        if len(bits) == 16 and type(bits) is list:
            cls.bits = bits.copy()
        else:
            print("Espera-se receber uma lista de 16 bits como parâmetro!")

    @classmethod
    def run(cls):
        bit = cls.bits[15]

        for i in range(16):
            cls.bits.append(bit)

# ExtensorDeSinal.set_bits(list("1001111111111110"))
# ExtensorDeSinal.run()
# print(ExtensorDeSinal.get())
