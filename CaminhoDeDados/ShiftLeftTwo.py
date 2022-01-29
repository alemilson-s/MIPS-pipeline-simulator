class ShiftLeftTwo:
    bits = list("00000000000000000000000000000000")

    @classmethod
    def get(cls):
        return cls.bits

    @classmethod
    def set_bits(cls, bits):
        if len(bits) == 32 and type(bits) is list:
            cls.bits = bits.copy()
        else:
            print("Espera-se receber uma lista de 32 bits como parâmetro!")

    @classmethod
    def run(cls):
        for i in range(2):
            cls.bits.pop()
            cls.bits.insert(0, '0')

# a = "00001111000111111111111110000000"
# ShiftLeftTwo.set_bits(list(a[::-1]))
# ShiftLeftTwo.run()
# print(ShiftLeftTwo.get())
