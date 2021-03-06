from CaminhoDeDados import BancoDeRegistradores
from CaminhoDeDados.Pipeline import Registradores


class Control:
    # Linhas de controle do estágio de execução/cálculo de endereço
    RegDst = False
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

    instruction = None

    @classmethod
    def get_reg_dst(cls):
        return cls.RegDst

    @classmethod
    def get_alu_op_1(cls):
        return cls.ALUOp1

    @classmethod
    def get_alu_op_0(cls):
        return cls.ALUOp0

    @classmethod
    def get_alu_src(cls):
        return cls.ALUSrc

    @classmethod
    def get_mem_read(cls):
        return cls.MemRead

    @classmethod
    def get_mem_write(cls):
        return cls.MemWrite

    @classmethod
    def get_reg_write(cls):
        return cls.RegWrite

    @classmethod
    def get_mem_to_reg(cls):
        return cls.MemtoReg

    @classmethod
    def set_instruction(cls, bits: list):
        cls.instruction = bits.copy()

    @classmethod
    def get_instruction(cls):
        return cls.instruction

    @classmethod
    def set_branch(cls, bit):
        cls.Branch = bit

    @classmethod
    def get_branch(cls):
        return cls.Branch

    @classmethod
    def run(cls):
        aux = cls.instruction[26:32]
        op = ''
        for valor in aux:
            op = op + op.join(valor)
        op = op[::-1]

        i = ''
        for valor in cls.instruction:
            i = i + i.join(valor)
        if i.__eq__("00000000000000000000000000000000"):
            cls.RegDst = False
            cls.ALUOp1 = False
            cls.ALUOp0 = False
            cls.ALUSrc = False
            cls.Branch = False
            cls.MemRead = False
            cls.MemWrite = False
            cls.RegWrite = False
            cls.MemtoReg = False

        elif op.__eq__('000000'):  # add, sub, and, or, slt, sll, jr -> R type
            cls.RegDst = True
            cls.ALUOp1 = True
            cls.ALUOp0 = False
            cls.ALUSrc = False
            cls.Branch = False
            cls.MemRead = False
            cls.MemWrite = False
            cls.RegWrite = True
            cls.MemtoReg = True
        elif op.__eq__('001000'):  # addi
            cls.RegDst = False  # seleciona rt como registrador destino
            cls.ALUOp1 = False
            cls.ALUOp0 = False
            cls.ALUSrc = True  # seleciona bits [0-15] para somar com rs na ALU
            cls.Branch = False  # não fazer desvio
            cls.MemRead = False  # não fazer leitura na memória
            cls.MemWrite = False  # não fazer escrita na memória
            cls.RegWrite = True  # fazer escrita no banco de registradores
            cls.MemtoReg = True  # selecionar valor calculado na ALU
        elif op.__eq__('100011'):  # lw
            cls.RegDst = False  # seleciona rt como registrador destino
            cls.ALUOp1 = False
            cls.ALUOp0 = False
            cls.ALUSrc = True  # selecioina bits [0-15] para somar com rs na ALU
            cls.Branch = False  # não fazer desvio
            cls.MemRead = True  # fazer leitura na memória
            cls.MemWrite = False  # não fazer escrita na memória
            cls.RegWrite = True  # fazer escita no banco de registradores
            cls.MemtoReg = False  # seleciona valor lido da memória
        elif op.__eq__('101011'):  # sw
            cls.ALUOp1 = False
            cls.ALUOp0 = False
            cls.ALUSrc = True  # seleciona bits [0-15] para somar com rs na ALU
            cls.Branch = False  # não fazer desvio
            cls.MemRead = False  # não fazer leitura na memória
            cls.MemWrite = True  # fazer escrita na memória
            cls.RegWrite = False  # não fazer escrita no banco de registradores
        elif op.__eq__('000100'):  # beq
            cls.ALUOp1 = False
            cls.ALUOp0 = True
            cls.ALUSrc = False  # seleciona registrador rt que veio do banco de registradores para somar na ALU
            cls.Branch = True  # fazer fesvio
            cls.MemRead = False  # não fazer leitura na memória
            cls.MemWrite = False  # não fazer escrita na memória
            cls.RegWrite = False  # não fazer escrita no banco de registradores
        elif op.__eq__('000101'):  # bne
            cls.ALUOp1 = False
            cls.ALUOp0 = True
            cls.ALUSrc = False  # seleciona registrador rt que veio do banco de registradores para somar na ALU
            cls.Branch = True  # fazer fesvio
            cls.MemRead = False  # não fazer leitura na memória
            cls.MemWrite = False  # não fazer escrita na memória
            cls.RegWrite = False  # não fazer escrita no banco de registradores
        elif op.__eq__('000010'):  # j:
            pass
        elif op.__eq__('000011'):  # jal
            pass

    @classmethod
    def zero(cls):
        cls.Branch = False
        cls.RegDst = False
        cls.ALUOp1 = False
        cls.ALUOp0 = False
        cls.ALUSrc = False
        cls.MemRead = False
        cls.MemWrite = False
        cls.RegWrite = False
        cls.MemtoReg = False


class FowardingUnit:
    Rs = None  # Número do registrador Rs vindo de ID/EX
    Rt = None  # Número do registrador Rt vindo de ID/EX
    Rd_ex_mem = None  # Número do registrador destino contido em EX/MEM
    Rd_mem_wb = None  # Número do registrador destino contido em MEM/WB
    RegWrite_ex_mem = False  # Sinal de controle indicando se instrução na etapa EX/MEM
    # faz escrita no banco de registradores
    RegWrite_mem_wb = False  # Sinal de controle indicando se instrução na etapa MEM/WB
    # faz escrita no banco de registradores

    FowardA = None  # Sinal de controle que indica qual operando usar na ALU como primeiro operando
    """
    FowardA = 00 -> ID/EX -> Primeiro operando vem do banco de registradores 
    FowardA = 01 -> EX/MEM -> Primeiro operando sofre fowarding do resultado anterior da ALU
    FowardA = 10 -> MEM/WB -> Primeiro operando sofre fowarding da memória ou de resultado anterior da ALU
    """
    FowardB = None  # Sinal de controle que indica qual operando usar na ALU como segundo operando
    """
    FowardB = 00 -> ID/EX -> Segundo operando vem do banco de registradores 
    FowardB = 01 -> EX/MEM -> Segundo operando sofre fowarding do resultado anterior da ALU
    FowardB = 10 -> MEM/WB -> Segundo operando sofre fowarding da memória ou de resultado anterior da ALU
    """

    @classmethod
    def get_rs(cls):
        return cls.Rs

    @classmethod
    def set_rs(cls, bits):
        if type(bits) is list:
            cls.Rs = ''
            for valor in bits:
                cls.Rs = cls.Rs + cls.Rs.join(valor)
            cls.Rs = cls.Rs[::-1]
        elif type(bits) is str:
            cls.Rs = bits
        else:
            print("Erro, espera-se receber uma lista como parâmetro -> setRs")

    @classmethod
    def get_rt(cls):
        return cls.Rt

    @classmethod
    def set_rt(cls, bits):
        if type(bits) is list:
            cls.Rt = ''
            for valor in bits:
                cls.Rt = cls.Rt + cls.Rt.join(valor)
            cls.Rt = cls.Rt[::-1]
        elif type(bits) is str:
            cls.Rt = bits
        else:
            print("Erro, espera-se receber uma lista como parâmetro -> setRt")

    @classmethod
    def get_rd_ex_mem(cls):
        return cls.Rd_ex_mem

    @classmethod
    def set_rd_ex_mem(cls, bits):
        if type(bits) is list:
            cls.Rd_ex_mem = ''
            for valor in bits:
                cls.Rd_ex_mem = cls.Rd_ex_mem + cls.Rd_ex_mem.join(valor)
            cls.Rd_ex_mem = cls.Rd_ex_mem[::-1]
        elif type(bits) is str:
            cls.Rd_ex_mem = bits
        else:
            print("Erro, espera-se receber uma lista como parâmetro -> setRd_ex_mem")

    @classmethod
    def get_rd_mem_wb(cls):
        return cls.Rd_mem_wb

    @classmethod
    def set_rd_mem_wb(cls, bits):
        if type(bits) is list:
            cls.Rd_mem_wb = ''
            for valor in bits:
                cls.Rd_mem_wb = cls.Rd_mem_wb + cls.Rd_mem_wb.join(valor)
            cls.Rd_mem_wb = cls.Rd_mem_wb[::-1]
        elif type(bits) is str:
            cls.Rd_mem_wb = bits
        else:
            print("Erro, espera-se receber uma lista como parâmetro -> setRd_mem_wb")

    @classmethod
    def get_reg_write_ex_mem(cls):
        return cls.RegWrite_ex_mem

    @classmethod
    def set_reg_write_ex_mem(cls, value):
        if type(value) is bool:
            cls.RegWrite_ex_mem = value

    @classmethod
    def get_reg_write_mem_wb(cls):
        return cls.RegWrite_mem_wb

    @classmethod
    def set_reg_write_mem_wb(cls, value):
        if type(value) is bool:
            cls.RegWrite_mem_wb = value

    @classmethod
    def get_foward_a(cls):
        return cls.FowardA

    @classmethod
    def get_foward_b(cls):
        return cls.FowardB

    @classmethod
    def run(cls):
        if cls.RegWrite_mem_wb and (
                not cls.Rd_mem_wb.__eq__(BancoDeRegistradores.Zero.get_id())) and cls.Rd_mem_wb.__eq__(cls.Rs) and (
                not cls.Rd_ex_mem.__eq__(cls.Rs)):
            cls.FowardA = "10"
        elif cls.RegWrite_ex_mem and (
                not cls.Rd_ex_mem.__eq__(BancoDeRegistradores.Zero.get_id())) and cls.Rd_ex_mem.__eq__(cls.Rs):
            cls.FowardA = "01"
        else:
            cls.FowardA = "00"

        if cls.RegWrite_mem_wb and (
                not cls.Rd_mem_wb.__eq__(BancoDeRegistradores.Zero.get_id())) and cls.Rd_mem_wb.__eq__(cls.Rt) and (
                not cls.Rd_ex_mem.__eq__(cls.Rt)
        ):
            cls.FowardB = "10"
        elif cls.RegWrite_ex_mem and (
                not cls.Rd_ex_mem.__eq__(BancoDeRegistradores.Zero.get_id())) and cls.Rd_ex_mem.__eq__(cls.Rt):
            cls.FowardB = "01"
        else:
            cls.FowardB = "00"


class HazardDetectionUnit:
    MemRead_id_ex = False  # Sinal que indica se será feita leitura na memória,
    # caso sinal esteja habilitado há chances de ocorrer stall
    Rd_id_ex = "00000"  # Vem da instrução contida em ID/EX, bits [16-20] -> Número do registrador
    Rs_if_id = "00000"  # Vem da instrução lida de IF/ID, bits [21-25] -> Número do registrador
    Rt_if_id = "00000"  # Vem da instrução lida de IF/ID, bits [16-20] -> Número do registrador
    PCWrite = True  # Sinal para indicar se PC deve ser escrito ou não
    if_id_Write = True  # Sinal para indicar se IF/ID deve ser escrito ou não

    @classmethod
    def get_mem_read_id_ex(cls):
        return cls.MemRead_id_ex

    @classmethod
    def set_mem_read_id_ex(cls, value):
        if type(value) is bool:
            cls.MemRead_id_ex = value

    @classmethod
    def get_rd_id_ex(cls):
        return cls.Rd_id_ex

    @classmethod
    def set_rd_id_ex(cls, bits):
        if type(bits) is list:
            cls.Rd_id_ex = ''
            for valor in bits:
                cls.Rd_id_ex = cls.Rd_id_ex + cls.Rd_id_ex.join(valor)
            cls.Rd_id_ex = cls.Rd_id_ex[::-1]

    @classmethod
    def get_rs_if_id(cls):
        return cls.Rs_if_id

    @classmethod
    def set_rs_if_id(cls, bits):
        if type(bits) is list:
            cls.Rs_if_id = ''
            for valor in bits:
                cls.Rs_if_id = cls.Rs_if_id + cls.Rs_if_id.join(valor)
            cls.Rs_if_id = cls.Rs_if_id[::-1]

    @classmethod
    def get_rt_if_id(cls):
        return cls.Rt_if_id

    @classmethod
    def set_rt_if_id(cls, bits):
        if type(bits) is list:
            cls.Rt_if_id = ''
            for valor in bits:
                cls.Rt_if_id = cls.Rt_if_id + cls.Rt_if_id.join(valor)
            cls.Rt_if_id = cls.Rt_if_id[::-1]

    @classmethod
    def get_pc_write(cls):
        return cls.PCWrite

    @classmethod
    def set_pc_write(cls, value):
        if type(value) is bool:
            cls.PCWrite = value

    @classmethod
    def get_if_id_write(cls):
        return cls.if_id_Write

    @classmethod
    def set_if_id_write(cls, value):
        if type(value) is bool:
            cls.if_id_Write = value

    @classmethod
    def run(cls):
        if cls.MemRead_id_ex and (cls.Rd_id_ex.__eq__(cls.Rs_if_id) or cls.Rd_id_ex.__eq__(cls.Rt_if_id)):
            cls.PCWrite = False
            cls.if_id_Write = False
            Control.zero()


class ALUControl:
    alu_control_output = None

    #   add, sub, and, or, slt, sll, addi, lw, sw, beq, bne, j, jr, jal.
    @classmethod
    def get_alu_control_output(cls):
        return cls.alu_control_output

    @classmethod
    def run(cls):
        alu_op0 = Registradores.IDEX.get_alu_op_0()
        alu_op1 = Registradores.IDEX.get_alu_op_1()

        if (not alu_op0) and (not alu_op1):  # lw/sw, addi
            cls.alu_control_output = '0010'
        elif alu_op0 and (not alu_op1):  # beq, bne
            cls.alu_control_output = '0110'
        elif (not alu_op0) and alu_op1:  # R type
            aux = Registradores.IDEX.get_instruction_0_15()
            aux = aux[0:6]
            funct = ''
            for indice in range(5, -1, -1):
                funct = funct + funct.join(aux[indice])
            if funct.__eq__('010000'):  # add
                cls.alu_control_output = '0010'
            elif funct.__eq__('100010'):  # sub
                cls.alu_control_output = '0110'
            elif funct.__eq__('100100'):  # and
                cls.alu_control_output = '0000'
            elif funct.__eq__('100101'):  # or
                cls.alu_control_output = '0001'
            elif funct.__eq__('101010'):  # slt
                cls.alu_control_output = '0111'
            elif funct.__eq__('001000'):  # jr
                cls.alu_control_output = '1010'
            elif funct.__eq__('000000'):  # sll
                cls.alu_control_output = '1111'


class And:
    Zero: bool = False
    Branch: bool = False

    @classmethod
    def set_zero(cls, sinal):
        cls.Zero = sinal

    @classmethod
    def set_branch(cls, sinal):
        cls.Branch = sinal

    @classmethod
    def get(cls):
        if cls.Zero and cls.Branch:
            return True
        else:
            return False
