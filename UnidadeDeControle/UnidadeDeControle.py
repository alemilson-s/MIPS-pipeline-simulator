from CaminhoDeDados import BancoDeRegistradores


class Control:
    # Linhas de controle do estágio de execução/cálculo de endereço
    RegDSt = False
    ALUOp1 = False
    ALUOp0 = False
    ALUSrc = False
    # Linas de controledo estágio de acesso à memória
    MemRead = False
    MemWrite = False
    # Linhas de controle do estágio de escrita do resultado
    RegWrite = False
    MemtoReg = False

    instruction = None

    @classmethod
    def run(cls, bits):
        pass

    @classmethod
    def zero(cls):
        cls.RegDSt = False
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
    RegWrite_ex_mem = None  # Sinal de controle indicando se instrução na etapa EX/MEM
    # faz escrita no banco de registradores
    RegWrite_mem_wb = None  # Sinal de controle indicando se instrução na etapa MEM/WB
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
    def run(cls):
        if cls.RegWrite_ex_mem and (
                not cls.Rd_ex_mem.equals(BancoDeRegistradores.zero.get_id())) and cls.Rd_ex_mem.equals(cls.Rs):
            cls.FowardA = "01"
        else:
            cls.FowardA = "00"

        if cls.RegWrite_ex_mem and (
                not cls.Rd_ex_mem.equals(BancoDeRegistradores.zero.get_id())) and cls.Rd_ex_mem.equals(cls.Rt):
            cls.FowardB = "01"
        else:
            cls.FowardB = "00"

        if cls.RegWrite_mem_wb and (
                not cls.Rd_mem_wb.equals(BancoDeRegistradores.zero.get_id())) and cls.Rd_mem_wb.equals(cls.Rs) and (
                not cls.Rd_ex_mem.equals(cls.Rs)):
            cls.FowardA = "10"
        else:
            cls.FowardA = "00"

        if cls.RegWrite_mem_wb and (
                not cls.Rd_mem_wb.equals(BancoDeRegistradores.zero.get_id())) and cls.Rd_mem_wb.equals(cls.Rt) and (
                not cls.Rd_ex_mem.equals(cls.Rt)
        ):
            cls.FowardB = "10"
        else:
            cls.FowardB = "00"


class HazardDetectionUnit:
    MemRead_id_ex = False  # Sinal que indica leitura na memória,
    # caso sinal esteja habilitado há chances de ocorrer ter stall
    Rd_id_ex = None  # Vem da instrução contida em ID/EX, bits [16-20] -> Número do registrador
    Rs_if_id = None  # Vem da instrução lida de IF/ID, bits [21-25] -> Número do registrador
    Rt_if_id = None  # Vem da instrução lida de IF/ID, bits [16-20] -> Número do registrador
    PCWrite = None  # Sinal para indicar se PC deve ser escrito ou não
    if_id_Write = None  # Sinal para indicar se IF/ID deve ser escrito ou não

    @classmethod
    def run(cls):
        if cls.MemRead_id_ex and (cls.Rd_id_ex.equals(cls.Rs_if_id) or cls.Rd_id_ex.equals(cls.Rt_if_id)):
            cls.PCWrite = False
            cls.if_id_Write = False
            Control.zero()
