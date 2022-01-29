from CaminhoDeDados.MemoriaDeInstrucoes import MemoriaDeInstrucoes
from UnidadeDeControle import UnidadeDeControle
from CaminhoDeDados.ALU import Alu
from CaminhoDeDados.BancoDeRegistradores import BancoDeRegistradores
from CaminhoDeDados.PC import Pc
from CaminhoDeDados import Somadores
from CaminhoDeDados.Pipeline import Registradores
from CaminhoDeDados import Multiplexadores
from CaminhoDeDados.ExtensorDeSinal import ExtensorDeSinal
from CaminhoDeDados.BancoDeRegistradores import T0
from CaminhoDeDados.BancoDeRegistradores import S0


class Arquivo:
    @classmethod
    def read(cls, path: str):
        linhas: list = []
        with open(path) as arquivo:
            for linha in arquivo:
                linhas.append(linha.replace("\n", ""))
        return linhas


if __name__ == "__main__":
    caminho_arquivo = "C:\\Users\\Israel Louback\\Documents\\teste.txt"
    caminho_arquivo_alemilson = 'C:\\Users\\ALEMILSON\\Downloads\\teste.txt.txt'

    linhas_arquivo = Arquivo.read(caminho_arquivo_alemilson)

    for line in linhas_arquivo:
        MemoriaDeInstrucoes.inserir_instrucao(line)
        # print(line)

    T0.set("00000000000000000000000000011000")
    S0.set("00000000000000100000000000011000")
    while MemoriaDeInstrucoes.its_valid(Pc.get_pc()):
        pc = Pc.get_pc()
        print("PC = " + pc)

        MemoriaDeInstrucoes.set_read_address(pc)
        instrucao = MemoriaDeInstrucoes.get_instruction()

        Somadores.PrimeiroSomador.set_primeiro_operando(pc)
        Somadores.PrimeiroSomador.run()
        pc_mais_quatro = Somadores.PrimeiroSomador.get()

        if UnidadeDeControle.HazardDetectionUnit.get_pc_write() is True:
            Pc.set_pc(pc_mais_quatro)

        Registradores.IFID.set_pc_more_4(pc_mais_quatro)
        Registradores.IFID.set_instruction(instrucao)

        if UnidadeDeControle.HazardDetectionUnit.get_if_id_write() is True:
            Registradores.IFID.set_instruction(instrucao)
            Registradores.IFID.set_pc_more_4(pc_mais_quatro)

        pc_mais_quatro = Registradores.IFID.get_pc_more_4()
        instrucao = Registradores.IFID.get_instruction()

        BancoDeRegistradores.set_read_register_1(instrucao[21:26])
        BancoDeRegistradores.set_read_register_2(instrucao[16:21])
        BancoDeRegistradores.set_write_register(Registradores.MEMWB.get_mux())
        BancoDeRegistradores.set_write_data(Multiplexadores.MuxReg.get())

        ExtensorDeSinal.set_bits(instrucao[0:16])
        ExtensorDeSinal.run()
        instrucao_0_15 = ExtensorDeSinal.get()

        instrucao_16_20 = instrucao[16:21]

        instrucao_11_15 = instrucao[11:16]

        UnidadeDeControle.Control.set_instruction(instrucao)
        UnidadeDeControle.Control.run()

        UnidadeDeControle.HazardDetectionUnit.set_mem_read_id_ex(Registradores.IDEX.get_mem_read())
        UnidadeDeControle.HazardDetectionUnit.set_rd_id_ex(Registradores.IDEX.get_instruction_16_20())
        UnidadeDeControle.HazardDetectionUnit.set_rs_if_id(Registradores.IFID.get_instruction()[21:26])
        UnidadeDeControle.HazardDetectionUnit.set_rt_if_id(Registradores.IFID.get_instruction()[16:21])
        UnidadeDeControle.HazardDetectionUnit.run()

        Registradores.IDEX.set_reg_dst(UnidadeDeControle.Control.get_reg_dst())
        Registradores.IDEX.set_alu_op_0(UnidadeDeControle.Control.get_alu_op_0())
        Registradores.IDEX.set_alu_op_1(UnidadeDeControle.Control.get_alu_op_1())
        Registradores.IDEX.set_alu_src(UnidadeDeControle.Control.get_alu_src())
        Registradores.IDEX.set_branch(UnidadeDeControle.Control.get_branch())
        Registradores.IDEX.set_mem_read(UnidadeDeControle.Control.get_mem_read())
        Registradores.IDEX.set_mem_write(UnidadeDeControle.Control.get_mem_write())
        Registradores.IDEX.set_reg_write(UnidadeDeControle.Control.get_reg_write())
        Registradores.IDEX.set_mem_to_reg(UnidadeDeControle.Control.get_memto_reg())
        Registradores.IDEX.set_pc_more_4(pc_mais_quatro)
        Registradores.IDEX.set_read_data_1(BancoDeRegistradores.get_read_data_1())
        Registradores.IDEX.set_read_data_2(BancoDeRegistradores.get_read_data_2())
        Registradores.IDEX.set_instruction_0_15(instrucao_0_15)
        Registradores.IDEX.set_instruction_16_20(instrucao_16_20)
        Registradores.IDEX.set_instruction_11_15(instrucao_11_15)
        Registradores.IDEX.set_read_register_1(instrucao[21:26])
        Registradores.IDEX.set_read_register_2(instrucao[16:21])

        UnidadeDeControle.FowardingUnit.set_rs(Registradores.IDEX.get_read_register_1())
        UnidadeDeControle.FowardingUnit.set_rt(Registradores.IDEX.get_read_register_2())
        UnidadeDeControle.FowardingUnit.set_rd_ex_mem(Registradores.EXMEM.get_mux_2())
        UnidadeDeControle.FowardingUnit.set_rd_mem_wb(Registradores.MEMWB.get_mux())
        UnidadeDeControle.FowardingUnit.set_reg_write_ex_mem(Registradores.EXMEM.get_reg_write())
        UnidadeDeControle.FowardingUnit.set_reg_write_mem_wb(Registradores.MEMWB.get_reg_write())
        UnidadeDeControle.FowardingUnit.run()

        Multiplexadores.MuxAlu1.set_bits_0(BancoDeRegistradores.get_read_data_1())
        Multiplexadores.MuxAlu1.set_bits_1(Multiplexadores.MuxReg.get())
        Multiplexadores.MuxAlu1.set_bits_2(Registradores.EXMEM.get_alu())

        Multiplexadores.MuxAlu2.set_bits_0(BancoDeRegistradores.get_read_data_2())
        Multiplexadores.MuxAlu2.set_bits_1(Multiplexadores.MuxReg.get())
        Multiplexadores.MuxAlu2.set_bits_2(Registradores.EXMEM.get_alu())

        Multiplexadores.MuxAlu1.set_sinal_de_controle(UnidadeDeControle.FowardingUnit.get_foward_a())
        Multiplexadores.MuxAlu2.set_sinal_de_controle(UnidadeDeControle.FowardingUnit.get_foward_b())

        Multiplexadores.MuxEXMEM.set_bits_0(Registradores.IDEX.get_instruction_16_20())  # rt
        Multiplexadores.MuxEXMEM.set_bits_1(Registradores.IDEX.get_instruction_11_15())  # rd

        Alu.set_data_1(Multiplexadores.MuxAlu1.get())
        Alu.set_data_2(Multiplexadores.MuxAlu2.get())

        UnidadeDeControle.ALUControl.run()
        Alu.set_alu_control_output()
        Alu.run()

        Registradores.EXMEM.set_branch(UnidadeDeControle.Control.get_branch())
        Registradores.EXMEM.set_mem_read(UnidadeDeControle.Control.get_mem_read())
        Registradores.EXMEM.set_mem_write(UnidadeDeControle.Control.get_mem_write())
        Registradores.EXMEM.set_reg_write(UnidadeDeControle.Control.get_reg_write())
        Registradores.EXMEM.set_mem_to_reg(UnidadeDeControle.Control.get_memto_reg())
        Registradores.EXMEM.set_somador(pc_mais_quatro)
        Registradores.EXMEM.set_zero(Alu.zero_is_activate())
        Registradores.EXMEM.set_alu(Alu.get_alu_output())
