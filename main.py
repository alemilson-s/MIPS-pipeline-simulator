from CaminhoDeDados import MemoriaDeInstrucoes
from UnidadeDeControle import UnidadeDeControle
from CaminhoDeDados import ALU
from CaminhoDeDados import BancoDeRegistradores
from CaminhoDeDados import PC
from CaminhoDeDados import Somadores


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
        MemoriaDeInstrucoes.MemoriaDeInstrucoes.inserir_instrucao(line)
        print(line)

    for i in range(8):
        MemoriaDeInstrucoes.MemoriaDeInstrucoes.set_read_address(PC.Pc.get_pc())
        print(MemoriaDeInstrucoes.MemoriaDeInstrucoes.get_instruction())
        Somadores.AdderPcMoreFour.set_primeiro_operando(PC.Pc.get_pc())
        Somadores.AdderPcMoreFour.run()
        PC.Pc.set_pc(Somadores.AdderPcMoreFour.get())
    # i = "00000010001100101000000100100100"
    # MemoriaDeInstrucoes.MemoriaDeInstrucoes.inserir_instrucao(i)
    # MemoriaDeInstrucoes.MemoriaDeInstrucoes.set_read_address("00000000000000000000000000000000")
    # print(MemoriaDeInstrucoes.MemoriaDeInstrucoes.get_instruction())
    # BancoDeRegistradores.S1.set("00000000000000000000000000001000")
    # BancoDeRegistradores.S2.set("00000000000000000000000000000011")
    # UnidadeDeControle.Control.set_instruction((list(i[::-1])))
    # UnidadeDeControle.Control.run()
    # UnidadeDeControle.HazardDetectionUnit.run()
    # UnidadeDeControle.FowardingUnit.run()
    # ALU.Alu.set_data_1(BancoDeRegistradores.S1.get())
    # ALU.Alu.set_data_2(BancoDeRegistradores.S2.get())
    # UnidadeDeControle.ALUControl.run()
    # ALU.Alu.set_alu_control_input()
    # ALU.Alu.run()
    # print(ALU.Alu.get_alu_output())
