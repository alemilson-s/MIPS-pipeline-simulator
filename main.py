from CaminhoDeDados import MemoriaDeInstrucoes
from UnidadeDeControle import UnidadeDeControle
from CaminhoDeDados import ALU
from CaminhoDeDados import BancoDeRegistradores


class Arquivo:
    @classmethod
    def read(cls, path: str):
        linhas: list = []
        with open(path) as arquivo:
            for linha in arquivo:
                linhas.append(linha.replace("\n", ""))
        return linhas


if __name__ == "__main__":
    # caminho_arquivo = "C:\\Users\\Israel Louback\\Documents\\teste.txt"
    # caminho_arquivoAle = '/home/alemilson/Downloads/a.txt'
    #
    # linhas_arquivo = Arquivo.read(caminho_arquivoAle)
    #
    # for linha in linhas_arquivo:
    #     MemoriaDeInstrucoes.MemoriaDeInstrucoes.inserir_instrucao(linha)
    #     print(linha)
    i = "00000010001100101000000100100100"
    MemoriaDeInstrucoes.MemoriaDeInstrucoes.inserir_instrucao(i)
    MemoriaDeInstrucoes.MemoriaDeInstrucoes.set_read_address("00000000000000000000000000000000")
    print(MemoriaDeInstrucoes.MemoriaDeInstrucoes.get_instruction())
    BancoDeRegistradores.S1.set("00000000000000000000000000001000")
    BancoDeRegistradores.S2.set("00000000000000000000000000000011")
    UnidadeDeControle.Control.set_instruction((list(i[::-1])))
    UnidadeDeControle.Control.run()
    UnidadeDeControle.HazardDetectionUnit.run()
    UnidadeDeControle.FowardingUnit.run()
    ALU.Alu.set_data_1(BancoDeRegistradores.S1.get())
    ALU.Alu.set_data_2(BancoDeRegistradores.S2.get())
    UnidadeDeControle.ALUControl.run()
    ALU.Alu.set_alu_control_input()
    ALU.Alu.run()
    print(ALU.Alu.get_alu_output())
