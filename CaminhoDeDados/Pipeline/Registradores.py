class if_id:
    pcMore_4 = None
    instruction = None

    @classmethod
    def setInstruction(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.instruction = bits.copy()
        elif len(bits) == 32:
            cls.instruction.clear()
            for valor in bits:
                cls.instruction.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getInstruction(cls):
        return cls.instruction

    @classmethod
    def setPcMore_4(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.pcMore_4 = bits.copy()
        elif len(bits) == 32:
            cls.pcMore_4.clear()
            for valor in bits:
                cls.pcMore_4.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getPcMore_4(cls):
        return cls.pcMore_4


class id_ex:
    # Linhas de controle do estágio de execução/cálculo de endereço
    RegDSt = None
    ALUOp1 = None
    ALUOp0 = None
    ALUSrc = None
    # Linas de controledo estágio de acesso à memória
    MemRead = None
    MemWrite = None
    # Linhas de controle do estágio de escrita do resultado
    RegWrite = None
    MemtoReg = None

    alu_1 = None
    alu_2 = None
    instruction_0_15 = None
    instruction_16_20 = None
    instruction_11_15 = None
    readRegister_1 = None
    readRegister_2 = None

    @classmethod
    def setRegDSt(cls, bit):
        cls.RegDSt = bit

    @classmethod
    def getRegDSt(cls):
        return cls.RegDSt

    @classmethod
    def setALUOp1(cls, bit):
        cls.ALUOp1 = bit

    @classmethod
    def getALUOp1(cls):
        return cls.ALUOp1

    @classmethod
    def setALUOp0(cls, bit):
        cls.ALUOp0 = bit

    @classmethod
    def getALUOp0(cls):
        return cls.ALUOp0

    @classmethod
    def setALUSrc(cls, bit):
        cls.ALUSrc = bit

    @classmethod
    def getALUSrc(cls):
        return cls.ALUSrc

    @classmethod
    def setMemRead(cls, bit):
        cls.MemRead = bit

    @classmethod
    def getMemRead(cls):
        return cls.MemRead

    @classmethod
    def setMemWrite(cls, bit):
        cls.MemWrite = bit

    @classmethod
    def getMemWrite(cls):
        return cls.MemWrite

    @classmethod
    def setRegWrite(cls, bit):
        cls.RegWrite = bit

    @classmethod
    def getRegWrite(cls):
        return cls.RegWrite

    @classmethod
    def setMemtoReg(cls, bit):
        cls.MemtoReg = bit

    @classmethod
    def getMemtoReg(cls):
        return cls.MemtoReg

    @classmethod
    def setAlu_1(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.alu_1 = bits.copy()
        elif len(bits) == 32:
            cls.alu_1.clear()
            for valor in bits:
                cls.alu_1.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getAlu_1(cls):
        return cls.alu_1

    @classmethod
    def setAlu_2(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.alu_2 = bits.copy()
        elif len(bits) == 32:
            cls.alu_2.clear()
            for valor in bits:
                cls.alu_2.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def setInstruction_0_15(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.instruction_0_15 = bits.copy()
        elif len(bits) == 32:
            cls.instruction_0_15.clear()
            for valor in bits:
                cls.instruction_0_15.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getInstruction_0_15(cls):
        return cls.instruction_0_15

    @classmethod
    def setInstruction_16_20(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.instruction_16_20 = bits.copy()
        elif len(bits) == 32:
            cls.instruction_16_20.clear()
            for valor in bits:
                cls.instruction_16_20.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getInstruction_16_20(cls):
        return cls.instruction_16_20

    @classmethod
    def setInstruction_11_15(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.instruction_11_15 = bits.copy()
        elif len(bits) == 32:
            cls.instruction_11_15.clear()
            for valor in bits:
                cls.instruction_11_15.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def getInstruction_11_15(cls, bits):
        return cls.instruction_11_15

    @classmethod
    def setReadRegister_1(cls, numero_registrador):
        if len(numero_registrador) == 5:
            if type(numero_registrador) == list:
                cls.readRegister_1 = ""
                for valor in numero_registrador:
                    cls.readRegister_1 = cls.readRegister_1 + "".join(valor)
                cls.readRegister_1 = cls.readRegister_1[::-1]
            else:
                cls.readRegister_1 = numero_registrador
        else:
            print("Número de bits deve ser igual à 5!")

    @classmethod
    def getReadRegister_1(cls):
        return cls.readRegister_1

    @classmethod
    def setReadRegister_2(cls, numero_registrador):
        if len(numero_registrador) == 5:
            if type(numero_registrador) == list:
                cls.readRegister_2 = ""
                for valor in numero_registrador:
                    cls.readRegister_2 = cls.readRegister_2 + "".join(valor)
                cls.readRegister_2 = cls.readRegister_2[::-1]
            else:
                cls.readRegister_2 = numero_registrador
        else:
            print("Número de bits deve ser igual à 5!")

    @classmethod
    def getReadRegister_2(cls):
        return cls.readRegister_2


class ex_mem:
    # Linhas de controle do estágio de escrita do resultado
    RegWrite = None
    MemtoReg = None

    dataMemory = None
    alu = None
    mux = None

    @classmethod
    def setRegWrite(cls, bit):
        cls.RegWrite = bit

    @classmethod
    def getRegWrite(cls):
        return cls.RegWrite

    @classmethod
    def setMemtoReg(cls, bit):
        cls.MemtoReg = bit

    @classmethod
    def getMemtoReg(cls):
        return cls.MemtoReg

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


class mem_wb:
    # Linas de controledo estágio de acesso à memória
    MemRead = None
    MemWrite = None
    # Linhas de controle do estágio de escrita do resultado
    RegWrite = None
    MemtoReg = None

    mux_1 = None
    mux_2 = None
    alu = None

    @classmethod
    def setMemRead(cls, bit):
        cls.MemRead = bit

    @classmethod
    def getMemRead(cls):
        return cls.MemRead

    @classmethod
    def setMemWrite(cls, bit):
        cls.MemWrite = bit

    @classmethod
    def getMemWrite(cls):
        return cls.MemWrite

    @classmethod
    def setRegWrite(cls, bit):
        cls.RegWrite = bit

    @classmethod
    def getRegWrite(cls):
        return cls.RegWrite

    @classmethod
    def setMemtoReg(cls, bit):
        cls.MemtoReg = bit

    @classmethod
    def getMemtoReg(cls):
        return cls.MemtoReg

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
