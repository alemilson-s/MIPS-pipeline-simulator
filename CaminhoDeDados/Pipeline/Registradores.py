class IFID:
    pc_more_4 = list("00000000000000000000000000000000")
    instruction = list("00000000000000000000000000000000")

    @classmethod
    def set_instruction(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.instruction = bits.copy()
        elif len(bits) == 32:
            cls.instruction.clear()
            for valor in bits:
                cls.instruction.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_instruction(cls):
        return cls.instruction

    @classmethod
    def set_pc_more_4(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.pc_more_4 = bits.copy()
        elif len(bits) == 32:
            cls.pc_more_4.clear()
            for valor in bits:
                cls.pc_more_4.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_pc_more_4(cls):
        return cls.pc_more_4


class IDEX:
    # Linhas de controle do estágio de execução/cálculo de endereço
    RegDSt = False
    ALUOp1 = False
    ALUOp0 = False
    ALUSrc = False
    # Linas de controledo estágio de acesso à memória
    Branch = False
    MemRead = False
    MemWrite = False
    # Linhas de controle do estágio de escrita do resultado
    RegWrite = False
    MemtoReg = False

    pc_more_4 = list("00000000000000000000000000000000")  # Pc + 4
    read_data_1 = list("00000000000000000000000000000000")  # bits do registrador rs
    read_data_2 = list("00000000000000000000000000000000")  # bits do registrador rt
    instruction_0_15 = list("0000000000000000")
    instruction_16_20 = list("01000")
    instruction_11_15 = list("01000")
    readRegister_1 = list("00000")  # instrução -> bits de [21-25]
    readRegister_2 = list("00000")  # instrução -> bits de [16-20]

    @classmethod
    def set_reg_dst(cls, bit):
        cls.RegDSt = bit

    @classmethod
    def get_reg_dst(cls):
        return cls.RegDSt

    @classmethod
    def set_alu_op_1(cls, bit):
        cls.ALUOp1 = bit

    @classmethod
    def get_alu_op_1(cls):
        return cls.ALUOp1

    @classmethod
    def set_alu_op_0(cls, bit):
        cls.ALUOp0 = bit

    @classmethod
    def get_alu_op_0(cls):
        return cls.ALUOp0

    @classmethod
    def set_alu_src(cls, bit):
        cls.ALUSrc = bit

    @classmethod
    def get_alu_src(cls):
        return cls.ALUSrc

    @classmethod
    def set_mem_read(cls, bit):
        cls.MemRead = bit

    @classmethod
    def get_mem_read(cls):
        return cls.MemRead

    @classmethod
    def set_mem_write(cls, bit):
        cls.MemWrite = bit

    @classmethod
    def get_mem_write(cls):
        return cls.MemWrite

    @classmethod
    def set_reg_write(cls, bit):
        cls.RegWrite = bit

    @classmethod
    def get_reg_write(cls):
        return cls.RegWrite

    @classmethod
    def set_mem_to_reg(cls, bit):
        cls.MemtoReg = bit

    @classmethod
    def get_mem_to_reg(cls):
        return cls.MemtoReg

    @classmethod
    def set_branch(cls, bit):
        cls.Branch = bit

    @classmethod
    def get_branch(cls):
        return cls.Branch

    @classmethod
    def set_read_data_1(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.read_data_1 = bits.copy()
        elif len(bits) == 32:
            cls.read_data_1.clear()
            for valor in bits:
                cls.read_data_1.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_read_data_1(cls):
        return cls.read_data_1

    @classmethod
    def set_read_data_2(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.read_data_2 = bits.copy()
        elif len(bits) == 32:
            cls.read_data_2.clear()
            for valor in bits:
                cls.read_data_2.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_read_data_2(cls):
        return cls.read_data_2

    @classmethod
    def set_instruction_0_15(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.instruction_0_15 = bits.copy()
        elif len(bits) == 32:
            cls.instruction_0_15.clear()
            for valor in bits:
                cls.instruction_0_15.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_instruction_0_15(cls):
        return cls.instruction_0_15

    @classmethod
    def set_instruction_16_20(cls, bits):
        if type(bits) == list and len(bits) == 5:
            cls.instruction_16_20 = bits.copy()
        elif len(bits) == 5:
            cls.instruction_16_20.clear()
            for valor in bits:
                cls.instruction_16_20.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 5!\n")

    @classmethod
    def get_instruction_16_20(cls):
        return cls.instruction_16_20

    @classmethod
    def set_instruction_11_15(cls, bits):
        if type(bits) == list and len(bits) == 5:
            cls.instruction_11_15 = bits.copy()
        elif len(bits) == 5:
            cls.instruction_11_15.clear()
            for valor in bits:
                cls.instruction_11_15.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 5!\n")

    @classmethod
    def get_instruction_11_15(cls):
        return cls.instruction_11_15

    @classmethod
    def set_read_register_1(cls, numero_registrador):
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
    def get_read_register_1(cls):
        return cls.readRegister_1

    @classmethod
    def set_read_register_2(cls, numero_registrador):
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
    def get_read_register_2(cls):
        return cls.readRegister_2

    @classmethod
    def set_pc_more_4(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.pc_more_4 = bits.copy()
        elif len(bits) == 32:
            cls.pc_more_4.clear()
            for valor in bits:
                cls.pc_more_4.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_pc_more_4(cls):
        return cls.pc_more_4


class EXMEM:
    # Linas de controledo estágio de acesso à memória
    Zero = False
    Branch = False
    MemRead = False
    MemWrite = False
    # Linhas de controle do estágio de escrita do resultado
    RegWrite = False
    MemtoReg = False

    somador = list("00000000000000000000000000000000")
    alu = list("00000000000000000000000000000000")
    mux_1 = list("00000000000000000000000000000000")
    mux_2 = list("00000")

    @classmethod
    def set_zero(cls, value):
        if type(value) is bool:
            cls.Zero = value

    @classmethod
    def get_zero(cls):
        return cls.Zero

    @classmethod
    def set_mem_read(cls, bit):
        cls.MemRead = bit

    @classmethod
    def get_mem_read(cls):
        return cls.MemRead

    @classmethod
    def set_mem_write(cls, bit):
        cls.MemWrite = bit

    @classmethod
    def get_mem_write(cls):
        return cls.MemWrite

    @classmethod
    def set_reg_write(cls, bit):
        cls.RegWrite = bit

    @classmethod
    def get_reg_write(cls):
        return cls.RegWrite

    @classmethod
    def set_mem_to_reg(cls, bit):
        cls.MemtoReg = bit

    @classmethod
    def get_mem_to_reg(cls):
        return cls.MemtoReg

    @classmethod
    def set_mux_1(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.mux_1 = bits.copy()
        elif len(bits) == 32:
            cls.mux_1.clear()
            for valor in bits:
                cls.mux_1.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_mux_1(cls):
        return cls.mux_1

    @classmethod
    def set_mux_2(cls, bits):
        if type(bits) == list and len(bits) == 5:
            cls.mux_2 = bits.copy()
        elif len(bits) == 32:
            cls.mux_2.clear()
            for valor in bits:
                cls.mux_2.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 5!\n")

    @classmethod
    def get_mux_2(cls):
        return cls.mux_2

    @classmethod
    def set_alu(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.alu = bits.copy()
        elif len(bits) == 32:
            cls.alu.clear()
            for valor in bits:
                cls.alu.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_alu(cls):
        return cls.alu

    @classmethod
    def set_somador(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.somador = bits.copy()
        elif len(bits) == 32:
            cls.somador.clear()
            for valor in bits:
                cls.somador.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_somador(cls):
        return cls.somador

    @classmethod
    def set_branch(cls, bit):
        cls.Branch = bit

    @classmethod
    def get_branch(cls):
        return cls.Branch


class MEMWB:
    # Linhas de controle do estágio de escrita do resultado
    RegWrite = False
    MemtoReg = False

    dataMemory = list("00000000000000000000000000000000")
    alu = list("00000000000000000000000000000000")
    mux = list("01000")

    @classmethod
    def set_reg_write(cls, bit):
        cls.RegWrite = bit

    @classmethod
    def get_reg_write(cls):
        return cls.RegWrite

    @classmethod
    def set_memto_reg(cls, bit):
        cls.MemtoReg = bit

    @classmethod
    def get_mem_to_reg(cls):
        return cls.MemtoReg

    @classmethod
    def set_data_memory(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.dataMemory = bits.copy()
        elif len(bits) == 32:
            cls.dataMemory.clear()
            for valor in bits:
                cls.dataMemory.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_data_memory(cls):
        return cls.dataMemory

    @classmethod
    def set_alu(cls, bits):
        if type(bits) == list and len(bits) == 32:
            cls.alu = bits.copy()
        elif len(bits) == 32:
            cls.alu.clear()
            for valor in bits:
                cls.alu.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 32!\n")

    @classmethod
    def get_alu(cls):
        return cls.alu

    @classmethod
    def set_mux(cls, bits):
        if type(bits) == list and len(bits) == 5:
            cls.mux = bits.copy()
        elif len(bits) == 32:
            cls.mux.clear()
            for valor in bits:
                cls.mux.insert(0, valor)
        else:
            print("Quantidade de bits tem de ser igual a 5!\n")

    @classmethod
    def get_mux(cls):
        return cls.mux
