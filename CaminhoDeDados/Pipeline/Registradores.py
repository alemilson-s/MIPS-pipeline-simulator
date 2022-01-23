class mem_wb:
    mux_1 = None
    mux_2 = None
    alu = None

    @classmethod
    def setMux_1(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.mux_1 = bits.copy()
        elif len(bits) == 32:
            cls.mux_1.clear()
            for valor in bits:
                cls.mux_1.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getMux_1(cls):

        return cls.mux_1

    @classmethod
    def setMux_2(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.mux_2 = bits.copy()
        elif len(bits) == 32:
            cls.mux_2.clear()
            for valor in bits:
                cls.mux_2.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getMux_2(cls):

        return cls.mux_2

    @classmethod
    def setAlu(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.alu = bits.copy()
        elif len(bits) == 32:
            cls.alu.clear()
            for valor in bits:
                cls.alu.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getAlu(cls):

        return cls.alu


class ex_mem:
    dataMemory = None
    alu = None
    mux = None

    @classmethod
    def setDataMemory(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.dataMemory = bits.copy()
        elif len(bits) == 32:
            cls.dataMemory.clear()
            for valor in bits:
                cls.dataMemory.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getDataMemory(cls):

        return cls.dataMemory

    @classmethod
    def setAlu(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.alu = bits.copy()
        elif len(bits) == 32:
            cls.alu.clear()
            for valor in bits:
                cls.alu.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getAlu(cls):

        return cls.alu

    @classmethod
    def setMux(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.mux = bits.copy()
        elif len(bits) == 32:
            cls.mux.clear()
            for valor in bits:
                cls.mux.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getMux(cls):

        return cls.mux
