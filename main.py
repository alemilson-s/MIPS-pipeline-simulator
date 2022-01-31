from CaminhoDeDados.MemoriaDeInstrucoes import MemoriaDeInstrucoes
from UnidadeDeControle import UnidadeDeControle
from CaminhoDeDados.ALU import Alu
from CaminhoDeDados.PC import Pc
from CaminhoDeDados import Somadores
from CaminhoDeDados.Pipeline import Registradores
from CaminhoDeDados import Multiplexadores
from CaminhoDeDados.ExtensorDeSinal import ExtensorDeSinal
from CaminhoDeDados.BancoDeRegistradores import *
from CaminhoDeDados.ShiftLeftTwo import ShiftLeftTwo
from CaminhoDeDados.MemoriaDeDados import MemoriaDeDados


class Arquivo:
    @classmethod
    def read(cls, path: str):
        linhas: list = []
        with open(path) as arquivo:
            for linha in arquivo:
                linhas.append(linha.replace("\n", ""))
        return linhas


class PrimeiraEtatpa:
    Somadores_PrimeiroSomador_get = list("00000000000000000000000000000000")
    MemoriaDeInstrucoes_get_instruction = list("00000000000000000000000000000000")


class SegundaEtapa:
    IFID_get_instruction = list("00000000000000000000000000000000")
    UnidadeDeControle_Control_get_reg_dst = False
    UnidadeDeControle_Control_get_alu_op_0 = False
    UnidadeDeControle_Control_get_alu_op_1 = False
    UnidadeDeControle_Control_get_alu_src = False
    UnidadeDeControle_Control_get_branch = False
    UnidadeDeControle_Control_get_mem_read = False
    UnidadeDeControle_Control_get_mem_write = False
    UnidadeDeControle_Control_get_reg_write = False
    UnidadeDeControle_Control_get_mem_to_reg = False
    IFID_get_pc_mais_quatro = list("00000000000000000000000000000000")
    BancoDeRegistradores_get_read_data_1 = list("00000000000000000000000000000000")
    BancoDeRegistradores_get_read_data_2 = list("00000000000000000000000000000000")
    instrucao_0_15 = list("00000000000000000000000000000000")
    instrucao_16_20 = list("00000")
    instrucao_11_15 = list("00000")
    IFID_get_instruction_21_25 = IFID_get_instruction[21:26]
    IFID_get_instruction_16_20 = IFID_get_instruction[16:21]


class TerceiraEtapa:
    Registradores_IDEX_get_branch = False
    Registradores_IDEX_get_mem_read = False
    Registradores_IDEX_get_mem_write = False
    Registradores_IDEX_get_reg_write = False
    Registradores_IDEX_get_mem_to_reg = False
    Somadores_SegundoSomador_get = list("00000000000000000000000000000000")
    Alu_zero_is_activate = False
    Alu_get_alu_output = list("00000000000000000000000000000000")
    Multiplexadores_MuxAlu2_get = list("00000000000000000000000000000000")
    Multiplexadores_MuxEXMEM_get = list("00000")
    Rs = list("00000")
    Rt = list("00000")


class QuartaEtapa:
    Registradores_EXMEM_get_reg_write = False
    Registradores_EXMEM_get_mem_to_reg = False
    MemoriaDeDados_get_read_data = list("00000000000000000000000000000000")
    Registradores_EXMEM_get_alu = list("00000000000000000000000000000000")
    Registradores_EXMEM_get_mux_2 = list("00000")


class QuintaEtapa:
    Registradores_MEMWB_get_mux = list("00000")
    Multiplexadores_MuxReg_get = list("00000000000000000000000000000000")
    Registradores_MEMWB_get_reg_write = False


def list_to_string(lista: list) -> str:
    result = ''
    for valor in lista:
        result += result.join(valor)
    return result[::-1]


def imprimir_dados():
    print(f"Pc = {Pc.get_pc()}")
    print(f"Banco de Registradores:")
    print(f"\t\t$v0 = {list_to_string(V0.get())}")
    print(f"\t\t$v1 = {list_to_string(V1.get())}")
    print(f"\t\t$a0 = {list_to_string(A0.get())}")
    print(f"\t\t$a1 = {list_to_string(A1.get())}")
    print(f"\t\t$a2 = {list_to_string(A2.get())}")
    print(f"\t\t$a3 = {list_to_string(A3.get())}")
    print(f"\t\t$t0 = {list_to_string(T0.get())}")
    print(f"\t\t$t1 = {list_to_string(T1.get())}")
    print(f"\t\t$t2 = {list_to_string(T2.get())}")
    print(f"\t\t$t3 = {list_to_string(T3.get())}")
    print(f"\t\t$t4 = {list_to_string(T4.get())}")
    print(f"\t\t$t5 = {list_to_string(T5.get())}")
    print(f"\t\t$t6 = {list_to_string(T6.get())}")
    print(f"\t\t$t7 = {list_to_string(T7.get())}")
    print(f"\t\t$s0 = {list_to_string(S0.get())}")
    print(f"\t\t$s1 = {list_to_string(S1.get())}")
    print(f"\t\t$s2 = {list_to_string(S2.get())}")
    print(f"\t\t$s3 = {list_to_string(S3.get())}")
    print(f"\t\t$s4 = {list_to_string(S4.get())}")
    print(f"\t\t$s5 = {list_to_string(S5.get())}")
    print(f"\t\t$s6 = {list_to_string(S6.get())}")
    print(f"\t\t$s7 = {list_to_string(S7.get())}")
    print(f"\t\t$s8 = {list_to_string(T8.get())}")
    print(f"\t\t$s9 = {list_to_string(T9.get())}")
    print(f"\t\t$sp = {list_to_string(Sp.get())}")
    print(f"\t\t$ra = {list_to_string(Ra.get())}\n")


if __name__ == "__main__":
    caminho_arquivo = "C:\\Users\\Israel Louback\\Documents\\teste.txt"
    caminho_arquivo_alemilson = 'C:\\Users\\ALEMILSON\\Downloads\\teste.txt.txt'

    linhas_arquivo = Arquivo.read(caminho_arquivo_alemilson)

    for line in linhas_arquivo:
        MemoriaDeInstrucoes.inserir_instrucao(line)
        # print(line)
    for i in range(5):
        MemoriaDeInstrucoes.inserir_instrucao("11111111111111111111111111111111")
    MemoriaDeDados.inicializar_memoria()

    while MemoriaDeInstrucoes.its_valid(Pc.get_pc()):
        # inicio primeira etapa escrita
        MemoriaDeInstrucoes.set_read_address(Pc.get_pc())

        Registradores.IFID.set_instruction(PrimeiraEtatpa.MemoriaDeInstrucoes_get_instruction)
        Registradores.IFID.set_pc_more_4(PrimeiraEtatpa.Somadores_PrimeiroSomador_get)
        # fim primeira etapa escrita

        # inicio segunda etapa escrita
        Registradores.IDEX.set_reg_dst(SegundaEtapa.UnidadeDeControle_Control_get_reg_dst)
        Registradores.IDEX.set_alu_op_0(SegundaEtapa.UnidadeDeControle_Control_get_alu_op_0)
        Registradores.IDEX.set_alu_op_1(SegundaEtapa.UnidadeDeControle_Control_get_alu_op_1)
        Registradores.IDEX.set_alu_src(SegundaEtapa.UnidadeDeControle_Control_get_alu_src)
        Registradores.IDEX.set_branch(SegundaEtapa.UnidadeDeControle_Control_get_branch)
        Registradores.IDEX.set_mem_read(SegundaEtapa.UnidadeDeControle_Control_get_mem_read)
        Registradores.IDEX.set_mem_write(SegundaEtapa.UnidadeDeControle_Control_get_mem_write)
        Registradores.IDEX.set_reg_write(SegundaEtapa.UnidadeDeControle_Control_get_reg_write)
        Registradores.IDEX.set_mem_to_reg(SegundaEtapa.UnidadeDeControle_Control_get_mem_to_reg)
        Registradores.IDEX.set_pc_more_4(SegundaEtapa.IFID_get_pc_mais_quatro)
        Registradores.IDEX.set_read_data_1(SegundaEtapa.BancoDeRegistradores_get_read_data_1)
        Registradores.IDEX.set_read_data_2(SegundaEtapa.BancoDeRegistradores_get_read_data_2)
        Registradores.IDEX.set_instruction_0_15(SegundaEtapa.instrucao_0_15)
        Registradores.IDEX.set_instruction_16_20(SegundaEtapa.instrucao_16_20)
        Registradores.IDEX.set_instruction_11_15(SegundaEtapa.instrucao_11_15)
        Registradores.IDEX.set_read_register_1(SegundaEtapa.IFID_get_instruction_21_25)
        Registradores.IDEX.set_read_register_2(SegundaEtapa.IFID_get_instruction_16_20)
        # fim segunda etapa escrita

        # inicio terceira etapa escrita
        Registradores.EXMEM.set_branch(TerceiraEtapa.Registradores_IDEX_get_branch)
        Registradores.EXMEM.set_mem_read(TerceiraEtapa.Registradores_IDEX_get_mem_read)
        Registradores.EXMEM.set_mem_write(TerceiraEtapa.Registradores_IDEX_get_mem_write)
        Registradores.EXMEM.set_reg_write(TerceiraEtapa.Registradores_IDEX_get_reg_write)
        Registradores.EXMEM.set_mem_to_reg(TerceiraEtapa.Registradores_IDEX_get_mem_to_reg)
        Registradores.EXMEM.set_somador(TerceiraEtapa.Somadores_SegundoSomador_get)
        Registradores.EXMEM.set_zero(TerceiraEtapa.Alu_zero_is_activate)
        Registradores.EXMEM.set_alu(TerceiraEtapa.Alu_get_alu_output)
        Registradores.EXMEM.set_mux_1(TerceiraEtapa.Multiplexadores_MuxAlu2_get)
        Registradores.EXMEM.set_mux_2(TerceiraEtapa.Multiplexadores_MuxEXMEM_get)
        # fim terceira etapa escrita

        # inicio quarta etapa escrita
        MemoriaDeDados.write()

        Registradores.MEMWB.set_reg_write(QuartaEtapa.Registradores_EXMEM_get_reg_write)
        Registradores.MEMWB.set_memto_reg(QuartaEtapa.Registradores_EXMEM_get_mem_to_reg)
        Registradores.MEMWB.set_data_memory(QuartaEtapa.MemoriaDeDados_get_read_data)
        Registradores.MEMWB.set_alu(QuartaEtapa.Registradores_EXMEM_get_alu)
        Registradores.MEMWB.set_mux(QuartaEtapa.Registradores_EXMEM_get_mux_2)
        # fim quarta etapa escrita

        # inicio quinta etapa escrita
        BancoDeRegistradores.set_write_register(QuintaEtapa.Registradores_MEMWB_get_mux)
        BancoDeRegistradores.set_write_data(QuintaEtapa.Multiplexadores_MuxReg_get)
        BancoDeRegistradores.set_reg_write(QuintaEtapa.Registradores_MEMWB_get_reg_write)
        BancoDeRegistradores.run()
        # fim quinta etapa escrita

        # inicio quinta etapa leitura
        Multiplexadores.MuxReg.set_bits_0(Registradores.MEMWB.get_data_memory())
        Multiplexadores.MuxReg.set_bits_1(Registradores.MEMWB.get_alu())
        Multiplexadores.MuxReg.set_sinal_de_controle(Registradores.EXMEM.get_mem_to_reg())

        QuintaEtapa.Registradores_MEMWB_get_mux = Registradores.MEMWB.get_mux()
        QuintaEtapa.Multiplexadores_MuxReg_get = Multiplexadores.MuxReg.get()
        QuintaEtapa.Registradores_MEMWB_get_reg_write = Registradores.MEMWB.get_reg_write()
        # fim quinta etapa leitura

        # inicio quarta etapa leitura
        MemoriaDeDados.set_address(Registradores.EXMEM.get_alu())
        MemoriaDeDados.set_write_date(Registradores.EXMEM.get_mux_1())
        MemoriaDeDados.set_mem_write(Registradores.EXMEM.get_mem_write())
        MemoriaDeDados.set_mem_read(Registradores.EXMEM.get_mem_read())
        MemoriaDeDados.read()

        QuartaEtapa.Registradores_EXMEM_get_reg_write = Registradores.EXMEM.get_reg_write()
        QuartaEtapa.Registradores_EXMEM_get_mem_to_reg = Registradores.EXMEM.get_mem_to_reg()
        QuartaEtapa.MemoriaDeDados_get_read_data = MemoriaDeDados.get_read_data()
        QuartaEtapa.Registradores_EXMEM_get_alu = Registradores.EXMEM.get_alu()
        QuartaEtapa.Registradores_EXMEM_get_mux_2 = Registradores.EXMEM.get_mux_2()
        # fim quarta etapa leitura

        # inicio terceira etapa leitura
        UnidadeDeControle.FowardingUnit.set_rs(Registradores.IDEX.get_read_register_1())
        UnidadeDeControle.FowardingUnit.set_rt(Registradores.IDEX.get_read_register_2())
        UnidadeDeControle.FowardingUnit.set_rd_ex_mem(Registradores.EXMEM.get_mux_2())
        UnidadeDeControle.FowardingUnit.set_rd_mem_wb(Registradores.MEMWB.get_mux())
        UnidadeDeControle.FowardingUnit.set_reg_write_ex_mem(Registradores.EXMEM.get_reg_write())
        UnidadeDeControle.FowardingUnit.set_reg_write_mem_wb(Registradores.MEMWB.get_reg_write())
        UnidadeDeControle.FowardingUnit.run()

        Multiplexadores.MuxAlu1.set_bits_0(Registradores.IDEX.get_read_data_1())
        Multiplexadores.MuxAlu1.set_bits_1(Multiplexadores.MuxReg.get())
        Multiplexadores.MuxAlu1.set_bits_2(Registradores.EXMEM.get_alu())

        Multiplexadores.MuxAlu2.set_bits_0(Registradores.IDEX.get_read_data_2())
        Multiplexadores.MuxAlu2.set_bits_1(Multiplexadores.MuxReg.get())
        Multiplexadores.MuxAlu2.set_bits_2(Registradores.EXMEM.get_alu())

        Multiplexadores.MuxAlu1.set_sinal_de_controle(UnidadeDeControle.FowardingUnit.get_foward_a())
        Multiplexadores.MuxAlu2.set_sinal_de_controle(UnidadeDeControle.FowardingUnit.get_foward_b())

        ShiftLeftTwo.set_bits(Registradores.IDEX.get_instruction_0_15())
        ShiftLeftTwo.run()

        Somadores.SegundoSomador.set_primeiro_operando(Registradores.IDEX.get_pc_more_4())
        Somadores.SegundoSomador.set_segundo_operando(ShiftLeftTwo.get())
        Somadores.SegundoSomador.run()

        Multiplexadores.MuxALUsrcToALU.set_bits_0(Multiplexadores.MuxAlu2.get())
        Multiplexadores.MuxALUsrcToALU.set_bits_1(Registradores.IDEX.get_instruction_0_15())
        Multiplexadores.MuxALUsrcToALU.set_sinal_de_controle(Registradores.IDEX.get_alu_src())

        Multiplexadores.MuxEXMEM.set_bits_0(Registradores.IDEX.get_instruction_16_20())  # rt
        Multiplexadores.MuxEXMEM.set_bits_1(Registradores.IDEX.get_instruction_11_15())  # rd
        Multiplexadores.MuxEXMEM.set_sinal_de_controle(Registradores.IDEX.get_reg_dst())
        # sinal indicando registrador destino

        Alu.set_data_1(Multiplexadores.MuxAlu1.get())
        Alu.set_data_2(Multiplexadores.MuxALUsrcToALU.get())

        UnidadeDeControle.ALUControl.run()
        Alu.set_alu_control_output()
        Alu.run()

        TerceiraEtapa.Registradores_IDEX_get_branch = Registradores.IDEX.get_branch()
        TerceiraEtapa.Registradores_IDEX_get_mem_read = Registradores.IDEX.get_mem_read()
        TerceiraEtapa.Registradores_IDEX_get_mem_write = Registradores.IDEX.get_mem_write()
        TerceiraEtapa.Registradores_IDEX_get_reg_write = Registradores.IDEX.get_reg_write()
        TerceiraEtapa.Registradores_IDEX_get_mem_to_reg = Registradores.IDEX.get_mem_to_reg()
        TerceiraEtapa.Somadores_SegundoSomador_get = Somadores.SegundoSomador.get()
        TerceiraEtapa.Alu_zero_is_activate = Alu.zero_is_activate()
        TerceiraEtapa.Alu_get_alu_output = Alu.get_alu_output()
        TerceiraEtapa.Multiplexadores_MuxAlu2_get = Multiplexadores.MuxAlu2.get()
        TerceiraEtapa.Multiplexadores_MuxEXMEM_get = Multiplexadores.MuxEXMEM.get()

        UnidadeDeControle.And.set_branch(Registradores.EXMEM.get_branch())
        UnidadeDeControle.And.set_zero(Registradores.EXMEM.get_zero())
        # fim terceira etapa leitura

        # inicio segunda etapa leitura
        instrucao = Registradores.IFID.get_instruction()
        SegundaEtapa.IFID_get_instruction = Registradores.IFID.get_instruction()

        BancoDeRegistradores.set_read_register_1(instrucao[21:26])
        BancoDeRegistradores.set_read_register_2(instrucao[16:21])

        ExtensorDeSinal.set_bits(instrucao[0:16])
        ExtensorDeSinal.run()

        UnidadeDeControle.Control.set_instruction(instrucao)
        UnidadeDeControle.Control.run()

        UnidadeDeControle.HazardDetectionUnit.set_mem_read_id_ex(Registradores.IDEX.get_mem_read())
        UnidadeDeControle.HazardDetectionUnit.set_rd_id_ex(Registradores.IDEX.get_instruction_16_20())
        UnidadeDeControle.HazardDetectionUnit.set_rs_if_id(Registradores.IFID.get_instruction()[21:26])
        UnidadeDeControle.HazardDetectionUnit.set_rt_if_id(Registradores.IFID.get_instruction()[16:21])
        UnidadeDeControle.HazardDetectionUnit.run()

        SegundaEtapa.UnidadeDeControle_Control_get_reg_dst = UnidadeDeControle.Control.get_reg_dst()
        SegundaEtapa.UnidadeDeControle_Control_get_alu_op_0 = UnidadeDeControle.Control.get_alu_op_0()
        SegundaEtapa.UnidadeDeControle_Control_get_alu_op_1 = UnidadeDeControle.Control.get_alu_op_1()
        SegundaEtapa.UnidadeDeControle_Control_get_alu_src = UnidadeDeControle.Control.get_alu_src()
        SegundaEtapa.UnidadeDeControle_Control_get_branch = UnidadeDeControle.Control.get_branch()
        SegundaEtapa.UnidadeDeControle_Control_get_mem_read = UnidadeDeControle.Control.get_mem_read()
        SegundaEtapa.UnidadeDeControle_Control_get_mem_write = UnidadeDeControle.Control.get_mem_write()
        SegundaEtapa.UnidadeDeControle_Control_get_reg_write = UnidadeDeControle.Control.get_reg_write()
        SegundaEtapa.UnidadeDeControle_Control_get_mem_to_reg = UnidadeDeControle.Control.get_mem_to_reg()
        SegundaEtapa.IFID_get_pc_mais_quatro = Registradores.IFID.get_pc_more_4()
        SegundaEtapa.BancoDeRegistradores_get_read_data_1 = BancoDeRegistradores.get_read_data_1()
        SegundaEtapa.BancoDeRegistradores_get_read_data_2 = BancoDeRegistradores.get_read_data_2()
        SegundaEtapa.instrucao_0_15 = ExtensorDeSinal.get()
        SegundaEtapa.instrucao_16_20 = instrucao[16:21]
        SegundaEtapa.instrucao_11_15 = instrucao[11:16]
        SegundaEtapa.IFID_get_instruction_21_25 = instrucao[21:26]
        SegundaEtapa.IFID_get_instruction_16_20 = instrucao[16:21]
        # fim segunda etapa leitura

        # inicio primeira etapa leitura
        Somadores.PrimeiroSomador.set_primeiro_operando(Pc.get_pc())
        Somadores.PrimeiroSomador.run()
        Multiplexadores.MuxPC.set_bits_0(Somadores.PrimeiroSomador.get())
        Multiplexadores.MuxPC.set_bits_1(Registradores.EXMEM.get_somador())
        Multiplexadores.MuxPC.set_sinal_de_controle(UnidadeDeControle.And.get())

        if UnidadeDeControle.HazardDetectionUnit.get_pc_write() and MemoriaDeInstrucoes.its_valid(Pc.get_pc()):
            Pc.set_pc(Multiplexadores.MuxPC.get())

        PrimeiraEtatpa.Somadores_PrimeiroSomador_get = Somadores.PrimeiroSomador.get()
        PrimeiraEtatpa.MemoriaDeInstrucoes_get_instruction = MemoriaDeInstrucoes.get_instruction()
        # fim primeira etapa leitura
        imprimir_dados()
